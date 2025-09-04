# BACKEND\app\modules\process\models\process.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel

class Process(BaseModel):
    __tablename__ = "processes"

    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Process {self.name}>"