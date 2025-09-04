# BACKEND\app\modules\process\models\process_step.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel

class ProcessStep(BaseModel):
    __tablename__ = "process_steps"

    process_id = db.Column(db.String(36), db.ForeignKey("processes.id"), nullable=False)
    step_number = db.Column(db.Integer, nullable=False)   # Ordre des étapes
    name = db.Column(db.String(100), nullable=False)      # Nom de l’étape
    description = db.Column(db.Text, nullable=True)

    # Relations
    process = db.relationship("Process", backref=db.backref("steps", lazy=True, order_by="ProcessStep.step_number"))

    def __repr__(self):
        return f"<ProcessStep {self.step_number}: {self.name}>"


    