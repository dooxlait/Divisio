# BACKEND\app\modules\planning\models\shift.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db

class Shift(BaseModel):
    __tablename__ = "shifts"

    name = db.Column(db.String(50), nullable=False)   # ex: équipe A matin
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    division_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("divisions.id"), nullable=True)
