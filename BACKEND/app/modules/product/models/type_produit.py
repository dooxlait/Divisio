# BACKEND/app/modules/product/models/type_produit.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel

class TypeProduit(BaseModel):
    __tablename__ = "type_produits"

    nom = db.Column(db.String(100), nullable=False, unique=True)

    produits = db.relationship("ProduitFini", back_populates="type_produit", lazy=True)

    def __repr__(self):
        return f"<TypeProduit {self.nom}>"
