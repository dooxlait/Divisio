# BACKEND\app\modules\quality\models\capa_action.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy import ForeignKey


class CAPAAction(BaseModel):
    __tablename__ = "capa_actions"

    action_type = db.Column(db.String(20), nullable=False)  
    # ex: "corrective", "preventive"

    description = db.Column(db.Text, nullable=False)

    status = db.Column(db.String(20), nullable=False, default="open")  
    # ex: "open", "in_progress", "completed", "ineffective"

    due_date = db.Column(db.Date, nullable=True)

    # --- Liens ---
    non_conformity_id = db.Column(db.String(36), ForeignKey("non_conformities.id"), nullable=False)
    assigned_to_id = db.Column(db.String(36), ForeignKey("employees.id"), nullable=True)

    def __repr__(self):
        return f"<CAPAAction type={self.action_type}, status={self.status}>"
