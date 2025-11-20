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

    # Clés étrangères
    id_categorie = db.Column(db.String(36), db.ForeignKey("categories.id"), nullable=True)
    id_unite = db.Column(db.String(36), db.ForeignKey("unites.id"), nullable=True)
    id_marque = db.Column(db.String(36), db.ForeignKey("marques.id"), nullable=True)
    id_fournisseur = db.Column(db.String(36), db.ForeignKey("fournisseurs.id"), nullable=True)

    # ===============================================================
    # RELATIONSHIPS
    # ===============================================================
    category = db.relationship("Category", back_populates="articles")
    marque = db.relationship("Marque", back_populates="articles")
    fournisseur = db.relationship("Fournisseur", back_populates="articles")
    unite = db.relationship("Unite", back_populates="articles", foreign_keys=[id_unite])

    compositions = db.relationship(
        "ArticleComposition",
        foreign_keys="ArticleComposition.article_id",
        back_populates="article",
        cascade="all, delete-orphan"
    )

    palettisation = db.relationship(
        "Palettisation",
        back_populates="article",
        uselist=False,
        cascade="all, delete-orphan"
    )

    caracteristique = db.relationship(
        "CaracteristiqueArticle",
        back_populates="article",
        uselist=False,
        cascade="all, delete-orphan"
    )

    stocks = db.relationship(
        "Stock",
        back_populates="article",
        cascade="all, delete-orphan"
    )

    production_orders = db.relationship(
        "ProductionOrder",
        back_populates="article",
        cascade="all, delete-orphan",
        lazy="dynamic"
    )
    
    # Recettes de production (produit fini)
    recettes = db.relationship(
        "ProductionRecipe",
        secondary="recipe_articles",
        back_populates="articles"
    )

    # ===============================================================
    # Méthodes utiles
    # ===============================================================
    def __repr__(self):
        return f"<Article {self.code} - {self.designation}>"

    @property
    def unite_code(self):
        return self.unite.code if self.unite else None
