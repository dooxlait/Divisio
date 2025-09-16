# BACKEND/app/modules/product/models/variante.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel


class Variante(BaseModel):
    __tablename__ = "variantes"

    # Nom de la variante : Nature, Sucré, Bicouche, Aromatisé, etc.
    nom = db.Column(db.String(50), nullable=False, unique=True)

    # Relation vers les produits finis
    produits = db.relationship("ProduitFini", back_populates="variante", lazy=True)

    def __repr__(self):
        return f"<Variante {self.nom}>"

