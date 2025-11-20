# BACKEND\app\modules\production\schemas\production_recipe\production_recipe_schema.py

from marshmallow import fields

from app.common.base.base_schema import BaseSchema
from app.core.extensions import db

class ProductionRecipeSchema(BaseSchema):
    """
    Schéma spécifique pour le modèle ProductionRecipe.
    On pourra ajouter ici des champs supplémentaires ou des nested fields.
    """
    # Ajoutez ici des champs spécifiques si nécessaire

    class Meta:
        model = None  # Remplacez par le modèle ProductionRecipe approprié
        load_instance = True
        include_fk = True
        sqla_session = db.session