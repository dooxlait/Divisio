from marshmallow import fields
from app.common.base.base_schema import BaseSchema
from app.core.extensions import db
from app.modules.production.models.recette_ingredient import RecetteIngredient

class RecetteIngredientSchema(BaseSchema):
    """
    Schéma pour représenter un ingrédient d'une recette.
    """

    # Relations utiles
    article = fields.Nested(
        "ArticleSchema",
        only=("code", "designation", "type_article"),
        dump_only=True
    )

    unite = fields.Nested(
        "UniteSchema",
        only=("id", "code", "libelle", "type_unite"),
        dump_only=True
    )

    class Meta:
        model = RecetteIngredient
        load_instance = True
        include_fk = True
        sqla_session = db.session