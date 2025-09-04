# BACKEND\app\modules\production\models\production_task.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy import ForeignKey

class ProductionTask(BaseModel):
    __tablename__ = "production_tasks"

    order_id = db.Column(db.String(36), ForeignKey("production_orders.id"), nullable=False)
    order = db.relationship("ProductionOrder", backref=db.backref("tasks", lazy=True))

    # --- Lien vers l’étape théorique du process ---
    process_step_id = db.Column(db.String(36), ForeignKey("process_steps.id"), nullable=False)
    process_step = db.relationship("ProcessStep", backref=db.backref("production_tasks", lazy=True))

    # --- Exécution réelle ---
    status = db.Column(db.String(20), nullable=False, default="pending")
    # pending / in_progress / done / failed

    started_at = db.Column(db.DateTime, nullable=True)
    finished_at = db.Column(db.DateTime, nullable=True)

    machine_id = db.Column(db.String(36), ForeignKey("machines.id"), nullable=True)
    machine = db.relationship("Machine", backref=db.backref("production_tasks", lazy=True))

    def __repr__(self):
        return f"<ProductionTask {self.id} - step={self.process_step_id} status={self.status}>"
