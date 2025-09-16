from app.core.extensions import db
from app.common.base.base_model import BaseModel

class CartonPalette(BaseModel):
    __tablename__ = "carton_palettes"

    carton_id = db.Column(db.String(36), db.ForeignKey("cartons.id"), nullable=False)
    palette_id = db.Column(db.String(36), db.ForeignKey("palettes.id"), nullable=False)

    carton = db.relationship("Carton", back_populates="palettes")
    palette = db.relationship("Palette", back_populates="cartons")
