# BACKEND\app\modules\factory\models\division_certification.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db


class DivisionCertification(BaseModel):
    __tablename__ = "division_certifications"

    division_id = db.Column(db.String(36), db.ForeignKey("divisions.id"), nullable=False)
    certification_id = db.Column(db.String(36), db.ForeignKey("certifications.id"), nullable=False)

    mandatory = db.Column(db.Boolean, default=True, nullable=False)  
    # True = obligatoire pour travailler dans la division
    # False = recommandé / optionnel

    # --- Relations ---
    division = db.relationship("Division", backref=db.backref("required_certifications", lazy=True))
    certification = db.relationship("Certification", backref=db.backref("required_for_divisions", lazy=True))

    __table_args__ = (
        db.UniqueConstraint("division_id", "certification_id", name="uq_division_certification"),
    )

    def __repr__(self):
        return f"<DivisionCertification division={self.division_id}, cert={self.certification_id}, mandatory={self.mandatory}>"
