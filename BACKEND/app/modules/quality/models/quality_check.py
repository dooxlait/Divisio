# BACKEND\app\modules\quality\models\quality_check.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy import ForeignKey


class QualityCheck(BaseModel):
    __tablename__ = "quality_checks"

    type = db.Column(db.String(50), nullable=False)  
    # ex: "incoming" (matière première), "in_process", "final"

    result = db.Column(db.String(20), nullable=False)  
    # ex: "passed", "failed", "rework", "blocked"

    notes = db.Column(db.Text, nullable=True)

    # --- Liens optionnels ---
    production_order_id = db.Column(db.String(36), ForeignKey("production_orders.id"), nullable=True)
    material_id = db.Column(db.String(36), ForeignKey("production_materials.id"), nullable=True)
    output_id = db.Column(db.String(36), ForeignKey("production_outputs.id"), nullable=True)
    machine_id = db.Column(db.String(36), ForeignKey("machines.id"), nullable=True)

    def __repr__(self):
        return f"<QualityCheck type={self.type}, result={self.result}>"
