from app.common.base.base_model import BaseModel
from app.core.extensions import db

class Article(BaseModel):
    __tablename__ = "articles"

    code = db.Column(db.String(50), nullable=False, unique=True)
    designation = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    id_categorie = db.Column(db.String(36), db.ForeignKey("categories.id"))
    id_unite = db.Column(db.String(36), db.ForeignKey("unites.id"))
    id_marque = db.Column(db.String(36), db.ForeignKey("marques.id"))
    id_fournisseur = db.Column(db.String(36), db.ForeignKey("fournisseurs.id"))

    # Relations
    category = db.relationship("Category", back_populates="articles")
    unite = db.relationship("Unite", back_populates="articles")
    marque = db.relationship("Marque", back_populates="articles")
    fournisseur = db.relationship("Fournisseur", back_populates="articles")

    # Liaisons vers ArticleComposition
    compositions = db.relationship(
        "ArticleComposition",
        foreign_keys="[ArticleComposition.article_id]",
        back_populates="article"
    )
    
    # Liaison vers Palettisation (1‑à‑1)
    palettisation = db.relationship(
        "Palettisation",
        back_populates="article",
        uselist=False,
        cascade="all, delete-orphan"
    )
    
    # Relation 1–1 vers les caractéristiques
    caracteristique = db.relationship(
        "CaracteristiqueArticle",
        uselist=False,
        back_populates="article",
        cascade="all, delete-orphan"
    )