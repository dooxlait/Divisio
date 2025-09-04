# BACKEND\app\modules\maintenance\models\work_order.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db


class WorkOrder(BaseModel):
    __tablename__ = "workorders"

    machine_id = db.Column(db.String(36), db.ForeignKey("machines.id"), nullable=False)
    site_id = db.Column(db.String(36), db.ForeignKey("sites.id"), nullable=False)
    division_id = db.Column(db.String(36), db.ForeignKey("divisions.id"), nullable=False)

    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(30), nullable=False, default="corrective")  # corrective, preventive, inspection...
    status = db.Column(db.String(20), nullable=False, default="draft")  # draft, planned, in_progress, completed, closed

    requested_by = db.Column(db.String(36), db.ForeignKey("employees.id"), nullable=False)
    assigned_to = db.Column(db.String(36), db.ForeignKey("employees.id"), nullable=True)

    planned_start_date = db.Column(db.DateTime, nullable=True)
    planned_end_date = db.Column(db.DateTime, nullable=True)
    actual_start_date = db.Column(db.DateTime, nullable=True)
    actual_end_date = db.Column(db.DateTime, nullable=True)

    # --- Relations ---
    machine = db.relationship("Machine", backref=db.backref("workorders", lazy=True))
    site = db.relationship("Site", backref=db.backref("workorders", lazy=True))
    division = db.relationship("Division", backref=db.backref("workorders", lazy=True))
    requester = db.relationship("Employee", foreign_keys=[requested_by], backref="requested_workorders")
    assignee = db.relationship("Employee", foreign_keys=[assigned_to], backref="assigned_workorders")

    def __repr__(self):
        return f"<WorkOrder {self.id} - {self.type} ({self.status})>"
