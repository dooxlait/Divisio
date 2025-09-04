# BACKEND\app\modules\maintenance\models\spare.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db


class SparePart(BaseModel):
    __tablename__ = "spare_parts"

    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=True)
    part_number = db.Column(db.String(100), nullable=True, unique=True)
    stock_quantity = db.Column(db.Integer, default=0)
    unit_of_measure = db.Column(db.String(20), nullable=False, default="pcs")
    location = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<SparePart {self.name} - {self.part_number}>"
