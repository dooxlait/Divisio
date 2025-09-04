# BACKEND\app\modules\maintenance\models\work_order_part.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db


class WorkOrderPart(BaseModel):
    __tablename__ = "workorder_parts"

    workorder_id = db.Column(db.String(36), db.ForeignKey("workorders.id"), nullable=False)
    part_id = db.Column(db.String(36), db.ForeignKey("spare_parts.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    # --- Relations ---
    workorder = db.relationship("WorkOrder", backref=db.backref("parts", lazy=True, cascade="all, delete-orphan"))
    part = db.relationship("SparePart", backref=db.backref("used_in", lazy=True))

    def __repr__(self):
        return f"<WorkOrderPart WO={self.workorder_id} Part={self.part_id} Qty={self.quantity}>"
