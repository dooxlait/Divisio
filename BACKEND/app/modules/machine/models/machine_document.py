# BACKEND\app\modules\machine\models\machine_document.py

from sqlalchemy import ForeignKey
from app.core.extensions import db
from app.common.base.base_model import BaseModel


class MachineDocument(BaseModel):
    __tablename__ = "machine_documents"

    type = db.Column(db.String(50), nullable=False)   # ex: "manuel", "schéma", "certificat"
    file_path = db.Column(db.String(255), nullable=False)  # chemin du fichier ou URL
    description = db.Column(db.String(255), nullable=True)

    machine_id = db.Column(db.String(36), ForeignKey("machines.id"), nullable=False)

    machine = db.relationship("Machine", back_populates="documents")

    def __repr__(self):
        return f"<MachineDocument {self.type} for Machine:{self.machine_id}>"
