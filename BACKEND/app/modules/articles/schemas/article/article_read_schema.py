# BACKEND\app\modules\articles\schemas\article\article_read_schema.py

from app.common.base.base_schema import BaseSchema
from app.core.extensions import ma
from app.modules.articles.models import Article
from app.modules.articles.schemas.marques import MarqueSchema
from app.modules.articles.schemas.unite import UniteSchema
from app.modules.articles.schemas.category import CategorySchema
from app.modules.articles.schemas.fournisseur import FournisseurSchema
from app.modules.articles.schemas.composition import ArticleCompositionSchema
from app.modules.articles.schemas.palettisation import PalettisationReadSchema
from app.modules.articles.schemas.caracteristique_article import CaracteristiqueArticleSchema
from marshmallow import fields, post_dump

class ArticleReadSchema(BaseSchema):
    """Schéma de lecture pour Article avec suppression des champs vides."""

    # Relations simples
    marque = ma.Nested(MarqueSchema, only=["id", "nom"])
    unite = ma.Nested(UniteSchema, only=["id", "code"])
    category = ma.Nested(CategorySchema, only=["id", "name"])
    fournisseur = ma.Nested(FournisseurSchema, only=["id", "nom"])
    palettisation = ma.Nested(
        PalettisationReadSchema, 
        dump_only=True, 
        only=["nb_colis_par_couche", "nb_couches_par_palette"]
    )
    caracteristique = ma.Nested(
        CaracteristiqueArticleSchema, 
        dump_only=True, 
        exclude=["id_article"]
    )

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
        sqla_session = None

    @post_dump
    def remove_none_fields(self, data, **kwargs):
        """Supprime toutes les clés dont la valeur est None."""
        return {k: v for k, v in data.items() if v is not None}

