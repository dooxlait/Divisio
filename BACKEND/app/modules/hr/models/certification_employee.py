# BACKEND\app\modules\hr\models\certification_employee.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db


class EmployeeCertification(BaseModel):
    __tablename__ = "employee_certifications"

    employee_id = db.Column(db.String(36), db.ForeignKey("employees.id"), nullable=False)
    certification_id = db.Column(db.String(36), db.ForeignKey("certifications.id"), nullable=False)

    obtained_date = db.Column(db.Date, nullable=False)    # Date d’obtention
    expiration_date = db.Column(db.Date, nullable=True)   # Date d’expiration (si applicable)

    # --- Relations ---
    employee = db.relationship("Employee", backref=db.backref("certifications", lazy=True))
    certification = db.relationship("Certification", backref=db.backref("employees", lazy=True))

    def __repr__(self):
        return f"<EmployeeCertification emp={self.employee_id}, cert={self.certification_id}>"
