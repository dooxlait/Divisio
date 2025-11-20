# BACKEND\app\modules\articles\schemas\article\article_schema.py

from marshmallow import fields

from app.common.base.base_schema import BaseSchema
from app.core.extensions import db

from app.modules.articles.models import Article
from app.modules.articles.schemas.caracteristique_article import CaracteristiqueArticleSchema

class ArticleSchema(BaseSchema):
    """
    Schéma spécifique pour le modèle Article.
    On pourra ajouter ici des champs supplémentaires ou des nested fields.
    """
    caracteristique = fields.Nested(
        CaracteristiqueArticleSchema,
        dump_only=True,
        only=['gamme']  # on limite aux champs nécessaires
    )
    class Meta:
        model = Article
        load_instance = True
        include_fk = True
        sqla_session = db.session  # Correctement placé au niveau de Meta