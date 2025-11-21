# app/modules/production/models/recette_ingredient.py
from app.common.base.base_model import BaseModel
from app.core.extensions import db

class RecetteIngredient(BaseModel):
    __tablename__ = "recette_ingredients"

    # Clés étrangères
    recipe_id = db.Column(db.String(36), db.ForeignKey("production_recipes.id"), nullable=False)
    article_id = db.Column(db.String(36), db.ForeignKey("articles.id"), nullable=False)  # L'Ingrédient (INPUT)
    unite_id = db.Column(db.String(36), db.ForeignKey("unites.id"), nullable=False)

    # ===============================================================
    # DONNÉES TECHNIQUES
    # ===============================================================
    
    # La quantité nécessaire pour réaliser la "taille_lot_ref" définie dans la Recette mère.
    # Exemple : Si la recette est définie pour 1000 Kg (Ref) et qu'il faut 50 Kg de Sucre.
    # Ici on stocke "50".
    quantity = db.Column(db.Numeric(12, 4), nullable=False)

    # Indique si cette quantité varie selon le volume produit.
    # True (Défaut) : Si je lance un OF de 2000 Kg (soit 2x la ref), il me faudra 100 Kg de sucre.
    # False : Quantité fixe par lot (ex: 1 dose de starter spécifique par cuve, peu importe le niveau).
    is_proportional = db.Column(db.Boolean, default=True)

    # ===============================================================
    # RELATIONSHIPS
    # ===============================================================
    recipe = db.relationship("ProductionRecipe", back_populates="ingredients")
    
    # L'article ingrédient (ex: Lait, Sucre, Fruit)
    article = db.relationship("Article") 
    unite = db.relationship("Unite")