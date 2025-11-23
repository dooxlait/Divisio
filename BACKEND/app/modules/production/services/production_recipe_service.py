# BACKEND\app\modules\production\services\production_recipe_service.py
import pandas as pd
from typing import Optional, Dict, Any, List, Union
from sqlalchemy import and_

from app.core.extensions import db

from app.modules.production.models.production_recipe import ProductionRecipe
from app.modules.articles.services.article_service  import lire_articles_filter

def read_recipe(filters: Optional[Dict[str, Any]] = None) -> Union[List[ProductionRecipe], ProductionRecipe, None]:
    """
    Lit les recettes.
    Retourne une LISTE de recettes, ou une RECETTE unique si filtré par 'code'.
    """
    # print(f"[INFO] Lecture des recettes avec filtres : {filters}")

    query = ProductionRecipe.query

    if filters:
        conditions = []
        for key, value in filters.items():
            # Vérification que l'attribut existe pour éviter les erreurs SQL
            if hasattr(ProductionRecipe, key):
                # Gestion basique des types (ex: conversion 'true'/'false' str en bool)
                if value == 'true': value = True
                elif value == 'false': value = False
                
                conditions.append(getattr(ProductionRecipe, key) == value)
            else:
                # On log juste un warning, on ne plante pas
                print(f"[WARN] Filtre ignoré : '{key}' n'existe pas sur Recette")
        
        if conditions:
            query = query.filter(and_(*conditions))

    try:
        if filters and "code" in filters:
            # Retourne un objet unique ou None
            return query.first() 
        
        # Retourne une liste
        return query.all()
    except Exception as e:
        raise RuntimeError(f"Erreur lecture recettes : {str(e)}")

def create_recipe(**data):
    """
    Crée une instance de recette et l'ajoute à la session.
    NE COMMIT PAS (pour permettre le bulk insert).
    """
    new_production_recipe = ProductionRecipe(**data)
    db.session.add(new_production_recipe)
    return new_production_recipe

def create_recipe_by_list(df):
    # Initialisation
    new_created = 0
    failed_rows = []
    
    # Nettoyage
    df = df.dropna(how="all")
    df.columns = df.columns.str.strip()

    # Parcours des lignes
    for index, row in df.iterrows():
        try:
            # Extraction sécurisée (évite les KeyErrors si une colonne manque)
            recipe_code = row.get("recipe_code")
            recipe_name = row.get("recipe_name", "")
            article_output_code = row.get("article_output_code", "")
            taille_lot_ref = row.get("taille_lot_ref", "")
            description = row.get("description", "")
            type_recette = row.get("type_recette", "process")

            if not recipe_code:
                raise ValueError("Le code recette (recipe_code) est obligatoire.")

            # Recherche de l'article (Optimisation: on appelle la fonction une seule fois)
            article_obj = lire_articles_filter(filters={"code": article_output_code})
            
            # Validation de l'article
            article_output_id = article_obj.id if article_obj else None
            
            # Optionnel : Lever une erreur si l'article n'existe pas ?
            if not article_output_id:
                raise ValueError(f"Article output code '{article_output_code}' introuvable.")

            data = {
                "code": recipe_code,
                "name": recipe_name,
                "version": 1,
                "is_active": True,
                "description": description,
                "taille_lot_ref": taille_lot_ref,
                "article_output_id": article_output_id,
                "recipe_type": type_recette
            }

            # Ajout à la session (sans commit)
            create_recipe(**data)
            new_created += 1

        except Exception as e:
            # En cas d'erreur sur une ligne, on l'ajoute aux échecs
            # Note: SQLAlchemy peut rollback automatiquement en cas d'erreur fatale au commit
            failed_rows.append({
                "row_index": index,
                "row_data": str(row.to_dict()), # Utile pour le debug
                "error": str(e)
            })

    # Commit final unique (Transaction atomique ou partielle selon logique souhaitée)
    try:
        if new_created > 0:
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        # Si le commit échoue, tout échoue
        return 0, [{"error": f"Erreur lors de l'enregistrement en base de données : {str(e)}"}]

    return new_created, failed_rows