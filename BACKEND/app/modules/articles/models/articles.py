from app.common.base.base_model import BaseModel
from app.core.extensions import db

class Article(BaseModel):
    __tablename__ = 'articles'

    code = db.Column(db.String(50), nullable=False, unique=True)
    designation = db.Column(db.String(255), nullable=False)
    ean = db.Column(db.String(20))
    is_active = db.Column(db.Boolean, default=True)

    id_categorie = db.Column(db.String(36), db.ForeignKey("categories.id"))
    id_unite = db.Column(db.String(36), db.ForeignKey("unites.id"))
    id_marque = db.Column(db.String(36), db.ForeignKey("marques.id"))  # <--- clé étrangère
    id_fournisseur = db.Column(db.String(36), db.ForeignKey("fournisseurs.id"))

    # Relations
    category = db.relationship("Category", back_populates="articles")
    unite = db.relationship("Unite", back_populates="articles")
    marque = db.relationship("Marque", back_populates="articles")  # <--- relation inverse


