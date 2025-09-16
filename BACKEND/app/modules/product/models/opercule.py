# BACKEND/app/modules/product/models/opercule.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel


class Opercule(BaseModel):
    __tablename__ = "opercules"

    # Matière : aluminium, plastique, papier, etc.
    matiere = db.Column(db.String(50), nullable=False)

    # Design ou information imprimée : logo, bio, promotion
    design = db.Column(db.String(100), nullable=True)

    # Relation vers les produits finis via ProduitEmballage (ou ProduitOpercule si table séparée)
    produits = db.relationship("ProduitEmballage", back_populates="opercule", lazy=True)

    def __repr__(self):
        return f"<Opercule {self.matiere} - {self.design}>"
