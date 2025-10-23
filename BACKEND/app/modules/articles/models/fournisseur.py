from app.core.extensions import db
from app.common.base.base_model import BaseModel

class Fournisseur(BaseModel):
    """
    Modèle représentant un fournisseur d'articles.
    Par exemple : Fournisseur A, Fournisseur B, etc.
    """
    __tablename__ = 'fournisseurs'

    nom = db.Column(db.String(100), nullable=False, unique=True)  # Nom unique du fournisseur
    adresse = db.Column(db.String(255), nullable=True)  # Adresse du fournisseur
    telephone = db.Column(db.String(20), nullable=True)  # Numéro de téléphone du fournisseur
    email = db.Column(db.String(100), nullable=True)  # Adresse email du fournisseur
    is_active = db.Column(db.Boolean, default=True)  # Indique si le fournisseur est actif

    # Relations
    articles = db.relationship("Article", back_populates="fournisseur")