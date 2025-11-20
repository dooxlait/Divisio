# app/modules/production/models/production_recipe.py
from app.common.base.base_model import BaseModel
from app.core.extensions import db

class ProductionRecipe(BaseModel):
    __tablename__ = "production_recipes"

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)

    # Many-to-many : une recette peut être utilisée par plusieurs articles finis
    articles = db.relationship(
        "Article",
        secondary="recipe_articles",
        back_populates="recettes"
    )

    # Ingrédients de la recette
    ingredients = db.relationship(
        "RecetteIngredient",
        back_populates="recipe",
        cascade="all, delete-orphan"
    )