from app.core.extensions import db
from app.common.base.base_model import BaseModel

class ProduitCarton(BaseModel):
    __tablename__ = "produit_cartons"

    carton_id = db.Column(db.String(36), db.ForeignKey("cartons.id"), nullable=False)
    produit_fini_id = db.Column(db.String(36), db.ForeignKey("produits_finis.id"), nullable=False)

    # Relations back_populates
    carton = db.relationship("Carton", back_populates="produits")
    produit_fini = db.relationship("ProduitFini", back_populates="cartons")