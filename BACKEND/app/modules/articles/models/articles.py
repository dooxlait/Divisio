# app/modules/articles/models/articles.py
from app.common.base.base_model import BaseModel
from app.core.extensions import db

class Article(BaseModel):
    __tablename__ = "articles"

    # ===============================================================
    # COLONNES
    # ===============================================================
    code = db.Column(db.String(50), nullable=False, unique=True)
    designation = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    type_article = db.Column(db.String(20)) # MP, BASE, VRAC, PF

    # Clés étrangères
    id_categorie = db.Column(db.String(36), db.ForeignKey("categories.id"), nullable=True)
    id_unite = db.Column(db.String(36), db.ForeignKey("unites.id"), nullable=True)
    id_marque = db.Column(db.String(36), db.ForeignKey("marques.id"), nullable=True)
    id_fournisseur = db.Column(db.String(36), db.ForeignKey("fournisseurs.id"), nullable=True)

    # ===============================================================
    # RELATIONSHIPS
    # ===============================================================
    
    # 1. Extension (Caractéristique)
    caracteristique = db.relationship(
        "CaracteristiqueArticle",
        back_populates="article",
        uselist=False,
        cascade="all, delete-orphan"
    )

    # 2. Process (Recettes) 
    # Le nom ici "recette_process" doit être identique au back_populates dans ProductionRecipe
    recette_process = db.relationship(
        "ProductionRecipe",
        back_populates="article_output",
        uselist=False, 
        cascade="all, delete-orphan"
    )

    # 3. Conditionnement (BOM)
    composition_enfants = db.relationship(
        "ArticleComposition",
        foreign_keys="ArticleComposition.article_parent_id",
        back_populates="article_parent",
        cascade="all, delete-orphan"
    )

    composition_parents = db.relationship(
        "ArticleComposition",
        foreign_keys="ArticleComposition.article_enfant_id",
        back_populates="article_enfant"
    )

    # 4. Production & Stocks
    production_orders = db.relationship("ProductionOrder", back_populates="article", lazy="dynamic")
    stocks = db.relationship("Stock", back_populates="article", cascade="all, delete-orphan")
    
    # Référentiels
    category = db.relationship("Category", back_populates="articles")
    marque = db.relationship("Marque", back_populates="articles")
    fournisseur = db.relationship("Fournisseur", back_populates="articles")
    unite = db.relationship("Unite", back_populates="articles", foreign_keys=[id_unite])
    
    # Palettisation
    palettisation = db.relationship("Palettisation", back_populates="article", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Article {self.code}>"

    @property
    def unite_code(self):
        return self.unite.code if self.unite else None

    @property
    def dlc(self):
        return self.caracteristique.DLC if self.caracteristique else 0
    
    @property
    def active_recipe(self):
        """Retourne la recette active (Process) ou None si c'est une MP"""
        # Si relation One-to-Many
        if self.recette_process:
             # Si c'est une liste, on cherche la version active
            if isinstance(self.recette_process, list):
                for r in self.recette_process:
                    if r.is_active: return r
            # Si c'est un objet unique (votre config actuelle uselist=False)
            else:
                return self.recette_process
        return None