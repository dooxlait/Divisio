# BACKEND\app\modules\articles\schemas\article\article_read_schema.py

from app.common.base.base_schema import BaseSchema
from app.core.extensions import db, ma

from app.modules.articles.models import Article
from app.modules.articles.schemas.marques import MarqueSchema
from app.modules.articles.schemas.unite import UniteSchema
from app.modules.articles.schemas.category import CategorySchema
from app.modules.articles.schemas.fournisseur import FournisseurSchema


class ArticleReadSchema(BaseSchema):
    """
    Schéma de lecture pour Article.
    Affiche les noms des entités liées au lieu de leurs IDs.
    """
    
    marque = ma.Nested(MarqueSchema, only=["id", "nom"])
    unite = ma.Nested(UniteSchema, only=["id", "code"])  # Schéma pour l'unité
    category = ma.Nested(CategorySchema, only=["id", "name"])
    fournisseur = ma.Nested(MarqueSchema, only=["id", "nom"])  # Schéma pour le fournisseur
    
    class Meta:
        model = Article
        load_instance = True
        include_fk = True
        sqla_session = db.session  # Correctement placé au niveau de Meta