# app/modules/production/schemas/production_order/production_order_schema.py
from marshmallow import fields

from app.common.base.base_schema import BaseSchema
from app.core.extensions import db

from app.modules.articles.schemas.unite.unite_schema import UniteSchema
from app.modules.articles.schemas.article.article_schema import ArticleSchema
from app.modules.production.models.production_order import ProductionOrder
from app.modules.factory.schemas.division import DivisionSchema

# --- IMPORT DU NOUVEAU SCHEMA ---
from app.modules.production.schemas.production_recipe.production_recipe_schema import ProductionRecipeSchema

class ProductionOrderSchema(BaseSchema):
    """
    Schéma spécifique pour le modèle ProductionOrder.
    """
    # Relation Article (déjà existant)
    article = fields.Nested(ArticleSchema, dump_only=True, only=['code', 'designation', 'caracteristique'])
    
    # Relation Unité (déjà existant)
    unite_article = fields.Nested(UniteSchema, dump_only=True, only=['code'], attribute='unite')

    # Relation Ligne/Atelier (déjà existant)
    ligne = fields.Nested(DivisionSchema, dump_only=True, only=['id', 'name'])
    
    # --- AJOUT DE LA RECETTE ---
    # dump_only=True : car on ne modifie pas la recette via l'endpoint de l'OF, on la lit juste.
    recipe = fields.Nested(ProductionRecipeSchema, dump_only=True, only=['id', 'code', 'name', 'version', 'taille_lot_ref'])

    class Meta:
        model = ProductionOrder
        load_instance = True
        include_fk = True
        sqla_session = db.session