# BACKEND\app\modules\quality\models\non_conformity.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy import ForeignKey


class NonConformity(BaseModel):
    __tablename__ = "non_conformities"

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    severity = db.Column(db.String(20), nullable=False)  
    # ex: "minor", "major", "critical"

    status = db.Column(db.String(20), nullable=False, default="open")  
    # ex: "open", "in_progress", "resolved", "closed"

    # --- Liens optionnels ---
    quality_check_id = db.Column(db.String(36), ForeignKey("quality_checks.id"), nullable=True)
    production_order_id = db.Column(db.String(36), ForeignKey("production_orders.id"), nullable=True)
    machine_id = db.Column(db.String(36), ForeignKey("machines.id"), nullable=True)

    def __repr__(self):
        return f"<NonConformity severity={self.severity}, status={self.status}>"
