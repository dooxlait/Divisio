# BACKEND\app\modules\machine\models\machine.py

from sqlalchemy import ForeignKey
from app.core.extensions import db
from app.common.base.base_model import BaseModel


class Machine(BaseModel):
    __tablename__ = "machines"

    name = db.Column(db.String(100), nullable=False)        # Nom de la machine ou composant
    type = db.Column(db.String(50), nullable=False)         # ex: "ligne", "machine", "module", "capteur"
    model = db.Column(db.String(100), nullable=True)        # Modèle
    serial_number = db.Column(db.String(100), unique=True, nullable=True)  # N° de série
    manufacturer = db.Column(db.String(100), nullable=True) # Fabricant / marque

    site_id = db.Column(db.String(36), ForeignKey("sites.id"), nullable=False)
    division_id = db.Column(db.String(36), ForeignKey("divisions.id"), nullable=False)

    # --- Auto-référencement ---
    parent_machine_id = db.Column(db.String(36), ForeignKey("machines.id"), nullable=True)
    children = db.relationship("Machine",
                               backref=db.backref("parent", remote_side="Machine.id"),
                               lazy=True)
    division = db.relationship("Division",
                        backref=db.backref("machines", lazy=True))

    # --- Relations ---
    documents = db.relationship("MachineDocument", back_populates="machine", lazy=True)

    def __repr__(self):
        return f"<Machine {self.name} ({self.type}) - SN:{self.serial_number}>"
