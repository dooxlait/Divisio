# BACKEND/app/modules/product/models/pot.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel


class Pot(BaseModel):
    __tablename__ = "pots"

    # Matière du pot : plastique, verre, carton, etc.
    matiere = db.Column(db.String(50), nullable=False)

    # Volume du pot en ml
    volume_ml = db.Column(db.Integer, nullable=False)

    # Relation vers les produits finis via ProduitEmballage
    produits = db.relationship("ProduitEmballage", back_populates="pot", lazy=True)

    def __repr__(self):
        return f"<Pot {self.matiere} - {self.volume_ml} ml>"
