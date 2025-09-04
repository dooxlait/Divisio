# BACKEND\app\modules\maintenance\models\work_order_task.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db


class WorkOrderTask(BaseModel):
    __tablename__ = "workorder_tasks"

    workorder_id = db.Column(db.String(36), db.ForeignKey("workorders.id"), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    sequence = db.Column(db.Integer, nullable=False, default=1)
    is_done = db.Column(db.Boolean, default=False)
    done_at = db.Column(db.DateTime, nullable=True)

    # --- Relations ---
    workorder = db.relationship("WorkOrder", backref=db.backref("tasks", lazy=True, cascade="all, delete-orphan"))

    def __repr__(self):
        return f"<WorkOrderTask {self.id} seq={self.sequence} done={self.is_done}>"
