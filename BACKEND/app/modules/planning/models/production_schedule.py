# BACKEND\app\modules\planning\models\production_schedule.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db

class ProductionSchedule(BaseModel):
    __tablename__ = "production_schedules"

    production_order_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("production_orders.id"), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)

    status = db.Column(db.String(20), default="planned")  
    # planned / in_progress / completed / delayed
