    
# app/modules/production/models/production_recipe.py
from app.common.base.base_model import BaseModel
from app.core.extensions import db

class ProductionRecipe(BaseModel):
    __tablename__ = "production_recipes"

    # ==========================================
    # IDENTIFICATION
    # ==========================================
    code = db.Column(db.String(50), nullable=False, unique=True) # ex: REC-FRAISE-V1
    name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.Integer, default=1) # Gestion des évolutions de recette
    is_active = db.Column(db.Boolean, default=True)
    description = db.Column(db.String(500), nullable=True)

    # ==========================================
    # LIEN PROCESS (OUTPUT)
    # ==========================================
    # Au lieu d'une liste d'articles, on définit ce que cette recette "sort" de la cuve.
    # Cela sera forcément un Article de type 'VRAC' ou 'BASE'.
    article_output_id = db.Column(db.String(36), db.ForeignKey("articles.id"), nullable=False)

    # Paramètre de référence pour les quantités des ingrédients
    # Ex: Les ingrédients sont définis pour "1000 kg" de produit fini (Taille de lot)
    taille_lot_ref = db.Column(db.Numeric(12, 4), default=1000) 

    # ==========================================
    # RELATIONS
    # ==========================================
    
    # 1. L'article produit par cette recette (Le Vrac ou la Base)
    article_output = db.relationship(
        "Article",
        back_populates="recette_process" # Doit matcher la relation dans Article
    )

    # 2. Les Ingrédients (Inputs)
    ingredients = db.relationship(
        "RecetteIngredient",
        back_populates="recipe",
        cascade="all, delete-orphan"
    )

    # 3. Historique : Quels OF ont utilisé cette recette ?
    production_orders = db.relationship(
        "ProductionOrder",
        back_populates="recipe",
        lazy="dynamic"
    )
    
    # 4. Spécifications Cibles de la Recette
    target_specs = db.relationship(
        "RecipeTargetSpec",
        back_populates="recipe",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Recipe {self.code} - {self.name}>"

  