from app.common.base.base_schema import BaseSchema
from app.core.extensions import ma
from app.modules.articles.models import Article
from app.modules.articles.schemas.marques import MarqueSchema
from app.modules.articles.schemas.unite import UniteSchema
from app.modules.articles.schemas.category import CategorySchema
from app.modules.articles.schemas.fournisseur import FournisseurSchema
from app.modules.articles.schemas.composition import ArticleCompositionSchema
from marshmallow import fields

class ArticleReadSchema(BaseSchema):
    """
    Schéma de lecture pour Article.
    Affiche les noms des entités liées et les composants.
    Gère correctement les UUID.
    """

    # Relations simples
    marque = ma.Nested(MarqueSchema, only=["id", "nom"])
    unite = ma.Nested(UniteSchema, only=["id", "code"])
    category = ma.Nested(CategorySchema, only=["id", "name"])
    fournisseur = ma.Nested(FournisseurSchema, only=["id", "nom"])

    # Relations composantes
    compositions = ma.Nested(ArticleCompositionSchema, many=True, dump_only=True)

    # Clés étrangères UUID sérialisées en string
    id_categorie = fields.String()
    id_unite = fields.String()
    id_marque = fields.String()
    id_fournisseur = fields.String()

    class Meta:
        model = Article
        load_instance = True
        include_fk = True
        sqla_session = None  # utilisera session globale de BaseSchema
