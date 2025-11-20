# app/modules/production/models/recipe_article.py
from app.common.base.base_model import BaseModel
from app.core.extensions import db

class RecipeArticle(BaseModel):
    __tablename__ = "recipe_articles"

    recipe_id = db.Column(db.String(36), db.ForeignKey("production_recipes.id"), nullable=False)
    article_id = db.Column(db.String(36), db.ForeignKey("articles.id"), nullable=False)