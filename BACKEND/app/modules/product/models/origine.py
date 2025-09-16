# BACKEND/app/modules/product/models/origine.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel


class Origine(BaseModel):
    __tablename__ = "origines"

    # Nom de l'origine : Brebis, Vache, Soja, etc.
    nom = db.Column(db.String(50), nullable=False, unique=True)

    # Relation vers les produits finis
    produits = db.relationship("ProduitFini", back_populates="origine", lazy=True)

    def __repr__(self):
        return f"<Origine {self.nom}>"
