# BACKEND/app/modules/production/models/production_output.py

from sqlalchemy import ForeignKey
from app.common.base.base_model import BaseModel
from app.core.extensions import db

class ProductionOutput(BaseModel):
    __tablename__ = "production_outputs"

    production_order_id = db.Column(db.String(36), ForeignKey("production_orders.id"), nullable=False)

    product_name = db.Column(db.String(100), nullable=False)   # Nom / référence produit
    lot_number = db.Column(db.String(50), nullable=True)       # N° de lot produit
    unit = db.Column(db.String(20), nullable=False)            # ex: "kg", "L", "pcs"

    quantity = db.Column(db.Float, nullable=False, default=0.0)
    status = db.Column(db.String(20), nullable=False, default="good")  # "good", "scrap", "rework"

    # --- Relations ---
    production_order = db.relationship("ProductionOrder", backref=db.backref("outputs", lazy=True))

    def __repr__(self):
        return f"<ProductionOutput {self.product_name} - {self.quantity} {self.unit} ({self.status})>"
