# BACKEND\app\modules\production\models\recipe_target_spec.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db

class RecipeTargetSpec(BaseModel):
    __tablename__ = "recipe_target_specs"

    recipe_id = db.Column(db.String(36), db.ForeignKey("production_recipes.id"), nullable=False)

    spec_name = db.Column(db.String(100), nullable=False)

    spec_unit_id = db.Column(db.String(36), db.ForeignKey("unites.id"), nullable=False)

    target_value = db.Column(db.Numeric(12, 4), nullable=False)
    target_min = db.Column(db.Numeric(12, 4), nullable=True)
    target_max = db.Column(db.Numeric(12, 4), nullable=True)

    tolerance = db.Column(db.Numeric(12, 4), nullable=True)

    recipe = db.relationship("ProductionRecipe", back_populates="target_specs")
    unit = db.relationship("Unite")