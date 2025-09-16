# BACKEND/app/modules/product/models/produit_fini.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel


class ProduitFini(BaseModel):
    __tablename__ = "produits_finis"

    # Nom commercial du produit
    nom = db.Column(db.String(150), nullable=False, unique=True)

    # Clés étrangères vers les tables de référence
    origine_id = db.Column(db.String(36), db.ForeignKey("origines.id"), nullable=False)
    type_produit_id = db.Column(db.String(36), db.ForeignKey("type_produits.id"), nullable=False)
    variante_id = db.Column(db.String(36), db.ForeignKey("variantes.id"), nullable=False)
    format_id = db.Column(db.String(36), db.ForeignKey("formats.id"), nullable=False)

    # Relations vers les tables de référence
    origine = db.relationship("Origine", back_populates="produits", lazy=True)
    type_produit = db.relationship("TypeProduit", back_populates="produits", lazy=True)
    variante = db.relationship("Variante", back_populates="produits", lazy=True)
    format = db.relationship("Format", back_populates="produits", lazy=True)

    # Relation vers les emballages unitaires
    emballages = db.relationship("ProduitEmballage", back_populates="produit", lazy=True)

    # Relation vers les cartons
    cartons = db.relationship("ProduitCarton", back_populates="produit_fini", lazy=True)

    def __repr__(self):
        return (
            f"<ProduitFini {self.nom} (origine={self.origine.nom}, type={self.type_produit.nom}, "
            f"variante={self.variante.nom}, format={self.format.poids_grammes} g)>"
        )
