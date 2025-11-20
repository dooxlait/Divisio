# app/modules/production/models/recette_ingredient.py
from app.common.base.base_model import BaseModel
from app.core.extensions import db

class RecetteIngredient(BaseModel):
    __tablename__ = "recette_ingredients"

    recipe_id = db.Column(db.String(36), db.ForeignKey("production_recipes.id"), nullable=False)
    article_id = db.Column(db.String(36), db.ForeignKey("articles.id"), nullable=False)  # ingrédient
    quantity = db.Column(db.Numeric(12, 4), nullable=False)  # ou pourcentage
    unite_id = db.Column(db.String(36), db.ForeignKey("unites.id"), nullable=False)

    # Relations
    recipe = db.relationship("ProductionRecipe", back_populates="ingredients")
    article = db.relationship("Article")
    unite = db.relationship("Unite")