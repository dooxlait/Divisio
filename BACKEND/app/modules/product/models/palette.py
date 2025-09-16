# BACKEND/app/modules/product/models/palette.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel


class Palette(BaseModel):
    __tablename__ = "palettes"

    # Type de palette : Europe, Demi, etc.
    type = db.Column(db.String(50), nullable=False)

    # Nombre de cartons par couche
    cartons_par_couche = db.Column(db.Integer, nullable=False)

    # Nombre de couches sur la palette
    nb_couches = db.Column(db.Integer, nullable=False)

    # Relation vers les cartons via la table d'association CartonPalette
    cartons = db.relationship("CartonPalette", back_populates="palette", lazy=True)

    def __repr__(self):
        return f"<Palette {self.type} ({self.cartons_par_couche}x{self.nb_couches})>"
