# BACKEND/app/modules/product/models/produit_emballage.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel


class ProduitEmballage(BaseModel):
    __tablename__ = "produit_emballages"

    # Clé étrangère vers le produit fini
    produit_fini_id = db.Column(
        db.String(36), db.ForeignKey("produits_finis.id"), nullable=False
    )

    # Clé étrangère vers le pot
    pot_id = db.Column(
        db.String(36), db.ForeignKey("pots.id"), nullable=False
    )

    # Clé étrangère vers la coiffe
    coiffe_id = db.Column(
        db.String(36), db.ForeignKey("coiffes.id"), nullable=False
    )

    # Clé étrangère vers l’opercule (optionnel)
    opercule_id = db.Column(
        db.String(36), db.ForeignKey("opercules.id"), nullable=True
    )

    # Relations
    produit = db.relationship("ProduitFini", back_populates="emballages", lazy=True)
    pot = db.relationship("Pot", back_populates="produits", lazy=True)
    coiffe = db.relationship("Coiffe", back_populates="produits", lazy=True)
    opercule = db.relationship("Opercule", back_populates="produits", lazy=True)

    def __repr__(self):
        return (
            f"<ProduitEmballage produit_id={self.produit_fini_id}, "
            f"pot_id={self.pot_id}, coiffe_id={self.coiffe_id}, opercule_id={self.opercule_id}>"
        )
