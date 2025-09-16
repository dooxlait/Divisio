# BACKEND/app/modules/product/models/coiffe.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel


class Coiffe(BaseModel):
    __tablename__ = "coiffes"

    # Matière du couvercle : aluminium, plastique, carton, etc.
    matiere = db.Column(db.String(50), nullable=False)

    # Design ou marque : neutre, marque interne, bio, etc.
    design = db.Column(db.String(100), nullable=True)

    # Relation vers les produits finis via ProduitEmballage
    produits = db.relationship("ProduitEmballage", back_populates="coiffe", lazy=True)

    def __repr__(self):
        return f"<Coiffe {self.matiere} - {self.design}>"
