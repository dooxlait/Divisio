# BACKEND\app\modules\production\schemas\production_order\production_order_schema.py
from marshmallow import fields

from app.common.base.base_schema import BaseSchema
from app.core.extensions import db

from app.modules.articles.schemas.unite.unite_schema import UniteSchema
from app.modules.articles.schemas.article.article_schema import ArticleSchema
from app.modules.production.models.production_order import ProductionOrder
from app.modules.factory.schemas.division import DivisionSchema

class ProductionOrderSchema(BaseSchema):
    """
    Schéma spécifique pour le modèle ProductionOrder.
    On pourra ajouter ici des champs supplémentaires ou des nested fields.
    """
    article = fields.Nested(ArticleSchema, dump_only=True, only=['code', 'designation', 'caracteristique'])
    unite_article = fields.Nested(UniteSchema, dump_only=True, only=['code'], attribute='unite')  # renommé ici
    ligne = fields.Nested(DivisionSchema, dump_only=True, only=['id', 'name'])
    
    class Meta:
        model = ProductionOrder
        load_instance = True
        include_fk = True
        sqla_session = db.session