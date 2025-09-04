# BACKEND\app\modules\maintenance\models\maintenance_request.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db


class MaintenanceRequest(BaseModel):
    __tablename__ = "maintenance_requests"

    machine_id = db.Column(db.String(36), db.ForeignKey("machines.id"), nullable=False)
    reporter_id = db.Column(db.String(36), db.ForeignKey("employees.id"), nullable=False)

    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(20), nullable=False, default="medium")  # low, medium, high, critical
    status = db.Column(db.String(20), nullable=False, default="new")  # new, approved, rejected, converted

    # --- Relations ---
    machine = db.relationship("Machine", backref=db.backref("maintenance_requests", lazy=True))
    reporter = db.relationship("Employee", backref=db.backref("reported_requests", lazy=True))

    def __repr__(self):
        return f"<MaintenanceRequest {self.id} for machine {self.machine_id}>"
