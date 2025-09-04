# BACKEND\app\modules\process\models\process_machine.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel

class ProcessMachine(BaseModel):
    __tablename__ = "process_machines"

    process_step_id = db.Column(db.String(36), db.ForeignKey("process_steps.id"), nullable=False)
    machine_id = db.Column(db.String(36), db.ForeignKey("machines.id"), nullable=False)

    parameters = db.Column(db.JSON, nullable=True)  # ex: {"flow_rate": "200 L/min"}

    # Relations
    process_step = db.relationship("ProcessStep", backref=db.backref("machines", lazy=True))
    
    # Pas besoin d'import direct, juste le nom de la classe
    machine = db.relationship("Machine", backref="process_machines")

    def __repr__(self):
        return f"<ProcessMachine step={self.process_step_id}, machine={self.machine_id}>"

    