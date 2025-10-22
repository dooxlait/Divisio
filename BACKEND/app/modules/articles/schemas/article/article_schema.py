# BACKEND\app\modules\articles\schemas\article\article_schema.py

from app.common.base.base_schema import BaseSchema
from app.core.extensions import db

from app.modules.articles.models import Article

class ArticleSchema(BaseSchema):
    """
    Schéma spécifique pour le modèle Article.
    On pourra ajouter ici des champs supplémentaires ou des nested fields.
    """
    class Meta:
        model = Article
        load_instance = True
        include_fk = True
        sqla_session = db.session  # Correctement placé au niveau de Meta