# BACKEND/app/modules/product/models/format.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel


class Format(BaseModel):
    __tablename__ = "formats"

    # Poids net ou volume (en grammes ou ml)
    poids_grammes = db.Column(db.Integer, nullable=False)

    # Description facultative (ex: "Petit format", "Standard")
    description = db.Column(db.String(100), nullable=True)

    # Relation vers les produits finis
    produits = db.relationship("ProduitFini", back_populates="format", lazy=True)

    def __repr__(self):
        return f"<Format {self.poids_grammes} g - {self.description}>"
