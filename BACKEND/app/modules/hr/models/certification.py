# BACKEND\app\modules\hr\models\certification.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db


class Certification(BaseModel):
    __tablename__ = "certifications"

    name = db.Column(db.String(100), nullable=False, unique=True)   # Nom de la certification
    description = db.Column(db.Text, nullable=True)                 # Détails (optionnel)
    validity_years = db.Column(db.Integer, nullable=True)           # Durée de validité (ex: 5 ans)

    def __repr__(self):
        return f"<Certification {self.name}>"