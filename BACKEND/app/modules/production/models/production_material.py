# BACKEND\app\modules\production\models\production_material.py 

from sqlalchemy import ForeignKey
from app.common.base.base_model import BaseModel
from app.core.extensions import db

class ProductionMaterial(BaseModel):
    __tablename__ = "production_materials"

    production_order_id = db.Column(db.String(36), ForeignKey("production_orders.id"), nullable=False)

    material_name = db.Column(db.String(100), nullable=False)   # Nom / référence de la matière
    lot_number = db.Column(db.String(50), nullable=True)        # N° de lot (traçabilité)
    unit = db.Column(db.String(20), nullable=False)             # ex: "kg", "L", "pcs"
    
    planned_quantity = db.Column(db.Float, nullable=False, default=0.0)
    consumed_quantity = db.Column(db.Float, nullable=True)

    # --- Relations ---
    production_order = db.relationship("ProductionOrder", backref=db.backref("materials", lazy=True))

    def __repr__(self):
        return f"<ProductionMaterial {self.material_name} - planned:{self.planned_quantity} {self.unit} consumed:{self.consumed_quantity}>"
