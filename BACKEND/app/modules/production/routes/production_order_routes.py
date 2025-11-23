from flask import Blueprint, request
from marshmallow import ValidationError
from collections import defaultdict

from datetime import datetime
from datetime import date, timedelta

from app.common.response.response import success_response, error_response
from app.common.helper.parse_helper import parse_filter_params
from app.common.helper.mrp import explode_ingredients_recursive, build_production_tree

from app.modules.articles.services.article_service import lire_articles_filter
from app.modules.production.services.production_order_service import create_order, read_orders
from app.modules.articles.services.unite_service import lire_unites_filter
from app.modules.factory.services.division_service import get_all_divisions

from app.modules.production.schemas import ProductionOrderSchema, ProductionOrderCreateSchema
from app.modules.production.models.production_order import ProductionOrder

from app.modules.articles.schemas.article.article_schema import ArticleSchema
from app.modules.production.schemas import ProductionOrderSchema, ProductionOrderCreateSchema


production_order_routes = Blueprint('production_order_routes', __name__)

@production_order_routes.route('/production_orders', methods=['GET'])
def get_production_orders():
    """
        Récupère la liste des ordres de production selon des filtres optionnels.

    Utilisation :
        Effectuer une requête GET vers l'endpoint '/production_orders' en ajoutant
        des paramètres de filtre en query string. Par exemple :
        
        GET /production_orders?status=completed&priority=true&start_date=2025-01-01
    """
    try:
        raw_filters = request.args.to_dict()
        filters = parse_filter_params(raw_filters)
        orders = read_orders(filters=filters)
        schema = ProductionOrderSchema(many=True)
        orders_data = schema.dump(orders)
        return success_response(
            data={"orders": orders_data},
            message="Liste des ordres de production récupérée avec succès",
            status_code=200
        )
    except Exception as e:
        return error_response(
            f"Erreur lors de la récupération des ordres de production : {str(e)}", 
            500
        )
    
@production_order_routes.route('/production_orders', methods=['POST'])
def create_production_order():
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return error_response("Données JSON manquantes", 400)

    # 1. Code article obligatoire
    code = data.get("code_article")
    if not code:
        return error_response("Le champ 'code_article' est obligatoire", 400)

    article = lire_articles_filter(filters={"code": code})
    if not article:
        return error_response(f"Article '{code}' introuvable", 404)

    # 2. Unité de l'OF (obligatoire ou par défaut)
    unite_code = data.get("unite_OF") or article.unite.code
    unite = lire_unites_filter(filters={"code": unite_code})
    if not unite:
        return error_response(f"Unité '{unite_code}' introuvable", 400)

    # 3. Date de plannification de l'OF (obligatoire, pas dans le passé)
    start_date_str = data.get("fabrication_start_date_planned")
    if not start_date_str:
        return error_response("Le champ 'fabrication_start_date_planned' est obligatoire", 400)
    try:
        start_date = date.fromisoformat(start_date_str)
        if start_date < date.today():
            return error_response("La date de début ne peut pas être dans le passé", 400)
    except ValueError:
        return error_response("Format de date invalide (AAAA-MM-JJ)", 400)

    # 4. DLC → calcul end_date
    dlc_days = article.caracteristique.DLC if article.caracteristique else 0
    end_date = start_date + timedelta(days=dlc_days)
    
    # 4.bis DGR → calcul end_date
    dgr_days = article.caracteristique.DGR if article.caracteristique else 0
    DGR_date = start_date + timedelta(days=dgr_days)
    
    # 5. Notes
    notes = data.get("notes", "")
    date_str = datetime.now().strftime("%Y-%m-%d")
    notes = f"[{date_str}] – {notes}" if notes else date_str
    if notes:
        notes += "\n"   
    
    # 6. Ligne de production (optionnelle)
    ligne_code = data.get("ligne")
    ligne = get_all_divisions(filters={"name": ligne_code, "type": "LIGNE"})[0] if ligne_code else None
    print(ligne.name)
    # ==============================================================================
    # 7. (NOUVEAU) Récupération de la recette associée à l'article
    # ==============================================================================
    recipe_id = None
    
    # On vérifie si l'article possède une relation 'recette_process'
    if article.recette_process:
        # CAS 1 : Si vous avez gardé uselist=False (Relation 1-1)
        # article.recette_process est directement l'objet recette
        recipe_id = article.recette_process.id
        
        # CAS 2 : Si vous avez changé pour uselist=True (Liste de versions)
        # Il faut filtrer pour trouver la recette active
        # if isinstance(article.recette_process, list):
        #     for r in article.recette_process:
        #         if r.is_active:
        #             recipe_id = r.id
        #             break

    # 8. Payload final
    payload = {
        "article_id": article.id,
        "unite_article_id": unite.id,
        
        # --- AJOUT ICI ---
        "recipe_id": recipe_id, 
        # -----------------
        
        "quantity_planned": int(data.get("quantity_planned") or 1),
        "fabrication_start_date_planned": start_date_str,
        "product_DLC": end_date.isoformat(),
        "product_DGR": DGR_date.isoformat(),
        "status": data.get("status", "planned"),
        "notes": notes or None,
        "ligne_id": ligne.id if ligne else None
    }

    try:
        order_data = ProductionOrderCreateSchema().load(payload)
        new_order = create_order(**order_data)

        return success_response(
            data={"order": ProductionOrderSchema().dump(new_order)},
            message="Ordre de fabrication créé avec succès",
            status_code=201
        )
    except ValidationError as e:
        return error_response(f"Erreur de validation : {e.messages}", 400)

# ==============================================================================
# ROUTE 3 : BESOINS JOURNALIERS (Vue d'ensemble par Produit Fini)
# ==============================================================================
@production_order_routes.route('/production/daily-needs', methods=['GET'])
def get_daily_requirements():
    """
    Calcule les besoins globaux pour une date donnée.
    Groupe les besoins process par Produit Fini (Arbres) et les emballages à plat.
    """
    # 1. Récupération de la date
    date_str = request.args.get('date')
    target_date = date.today()
    if date_str:
        try:
            target_date = date.fromisoformat(date_str)
        except ValueError:
            return error_response("Format de date invalide (AAAA-MM-JJ)", 400)

    # 2. Récupérer les OFs
    ofs = ProductionOrder.query.filter(
        ProductionOrder.fabrication_start_date_planned == target_date,
        ProductionOrder.status != 'cancelled'
    ).all()

    if not ofs:
        return success_response(
            data={"date": target_date.isoformat(), "production_process": [], "packaging_needs": []}, 
            message=f"Aucun OF prévu pour le {target_date}"
        )

    # 3. Agrégation des données
    # Pour le process, on cumule d'abord les quantités par article fini pour ne faire qu'un seul arbre par produit
    products_to_make_mass = defaultdict(float) # Stocke la masse totale (Kg/L) par code article
    article_map = {} # Pour garder l'objet article en mémoire
    
    # Pour le packaging, on cumule tout à plat
    needs_packaging = defaultdict(dict)

    for of in ofs:
        quantity_of = float(of.quantity_planned)

        # --- A. Préparation Process (Conversion Colis -> Masse) ---
        poids_unitaire = 1.0
        if of.article.caracteristique and hasattr(of.article.caracteristique, 'poids_net'):
            poids_unitaire = float(of.article.caracteristique.poids_net or 1.0)
        
        qty_masse = quantity_of * poids_unitaire
        
        # On ajoute à la liste de production globale du jour
        products_to_make_mass[of.article.code] += qty_masse
        article_map[of.article.code] = of.article

        # --- B. Calcul Packaging (BOM) ---
        if of.article.composition_enfants:
            for comp in of.article.composition_enfants:
                child = comp.article_enfant
                if child:
                    code = child.code
                    qty_pack = quantity_of * float(comp.quantite or 0)
                    
                    if code not in needs_packaging:
                        needs_packaging[code] = {
                            "code": code,
                            "designation": child.designation,
                            "quantity": 0.0,
                            "unit": child.unite_code or "U",
                            "type": "packaging"
                        }
                    needs_packaging[code]["quantity"] += qty_pack

    # 4. Construction des Arbres Process (Un par type de produit fini)
    production_trees = []
    for code_article, total_mass in products_to_make_mass.items():
        article = article_map[code_article]
        # Appel de la fonction helper
        tree = build_production_tree(article, total_mass)
        # On ajoute une info pour dire que c'est un cumul
        tree["designation"] = f"{article.designation} (CUMUL JOURNÉE)"
        production_trees.append(tree)

    # 5. Retour
    return success_response(
        data={
            "date": target_date.isoformat(),
            "of_count": len(ofs),
            "production_process": production_trees,        # Liste d'arbres
            "packaging_needs": list(needs_packaging.values()) # Liste plate
        },
        message="Calcul des besoins journaliers effectué"
    )


# ==============================================================================
# ROUTE 4 : BESOINS D'UN OF SPÉCIFIQUE (Détail unitaire)
# ==============================================================================
@production_order_routes.route('/production_orders/<string:of_id>/requirements', methods=['GET'])
def get_production_order_requirements(of_id):
    """
    Récupère les besoins détaillés pour un OF spécifique.
    """
    # 1. Récupérer l'OF
    order = ProductionOrder.query.get(of_id)
    if not order:
        return error_response("Ordre de fabrication introuvable", 404)

    quantity_planned = float(order.quantity_planned)
    
    # 2. Conversion OF -> Masse (Unités Recette)
    poids_unitaire = 1.0
    if order.article.caracteristique and hasattr(order.article.caracteristique, 'poids_net'):
        poids_unitaire = float(order.article.caracteristique.poids_net or 1.0)
    
    qty_masse_totale = quantity_planned * poids_unitaire

    # 3. A. CALCUL PROCESS (Arbre unique)
    process_tree = build_production_tree(order.article, qty_masse_totale)
    
    # Ajout d'infos contextuelles sur la racine de l'arbre
    process_tree["quantity_of"] = quantity_planned
    process_tree["unit_of"] = order.unite_article.code if order.unite_article else "U"

    # 4. B. CALCUL PACKAGING (Liste plate)
    packaging_list = []
    if order.article.composition_enfants:
        for comp in order.article.composition_enfants:
            child = comp.article_enfant
            if child:
                qty_pack = quantity_planned * float(comp.quantite or 0)
                packaging_list.append({
                    "code": child.code,
                    "designation": child.designation,
                    "quantity": round(qty_pack, 4),
                    "unit": child.unite_code or "U",
                    "type": "packaging"
                })

    return success_response(
        data={
            "of_reference": order.reference,
            "status": order.status,
            "process_requirements": process_tree,      # Objet Arbre unique
            "packaging_requirements": packaging_list   # Liste plate
        },
        message="Calcul des besoins pour l'OF effectué avec succès"
    )