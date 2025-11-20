from flask import Blueprint, request
from marshmallow import ValidationError

from datetime import datetime
from datetime import date, timedelta

from app.common.response.response import success_response, error_response
from app.common.helper.parse_helper import parse_filter_params

from app.modules.articles.services.article_service import lire_articles_filter
from app.modules.production.services.production_order_service import create_order, read_orders
from app.modules.articles.services.unite_service import lire_unites_filter
from app.modules.factory.services.division_service import get_all_divisions

from app.modules.production.schemas import ProductionOrderSchema, ProductionOrderCreateSchema
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
    # 6. Payload final
    payload = {
        "article_id": article.id,
        "unite_article_id": unite.id,
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

    