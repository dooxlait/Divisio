# BACKEND\app\modules\planning\models\schedule_allocation.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db

class ScheduleAllocation(BaseModel):
    __tablename__ = "schedule_allocations"

    schedule_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("production_schedules.id"), nullable=False)
    machine_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("machines.id"), nullable=True)
    division_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("divisions.id"), nullable=True)
    shift_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("shifts.id"), nullable=True)

    priority = db.Column(db.Integer, default=1)  # pour l’ordonnancement interne
