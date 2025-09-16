# models/carton.py
from app.core.extensions import db
from app.common.base.base_model import BaseModel

class Carton(BaseModel):
    __tablename__ = "cartons"

    nom = db.Column(db.String(100), nullable=False, unique=True)
    capacite = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=True)

    # ⚡ Important : mettre le nom de la classe en string pour éviter l'import circulaire
    produits = db.relationship("ProduitCarton", back_populates="carton", lazy=True)
    palettes = db.relationship("CartonPalette", back_populates="carton", lazy=True)

    def __repr__(self):
        return f"<Carton {self.nom} (capacité={self.capacite})>"