# BACKEND\app\modules\production\schemas\recipe_target_spec\recipe_target_spec_schema.py

from marshmallow import fields

from app.common.base.base_schema import BaseSchema
from app.core.extensions import db
from app.modules.production.models.recipe_target_spec import RecipeTargetSpec

class RecipeTargetSpecSchema(BaseSchema): 
    """
    Schéma spécifique pour le modèle RecetteIngredient.
    On pourra ajouter ici des champs supplémentaires ou des nested fields.
    """
    # Ajoutez ici des champs spécifiques si nécessaire

    class Meta:
        model = RecipeTargetSpec  
        load_instance = True
        include_fk = True
        sqla_session = db.session