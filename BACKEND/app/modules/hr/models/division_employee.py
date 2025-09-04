# BACKEND/app/modules/hr/models/division_employee.py

from sqlalchemy import ForeignKey, UniqueConstraint
from app.common.base.base_model import BaseModel
from app.core.extensions import db


class DivisionEmployee(BaseModel):
    __tablename__ = "division_employees"
    __table_args__ = (
        UniqueConstraint("employee_id", "division_id", "start_date", name="uq_employee_division"),
    )

    employee_id = db.Column(db.String(36), ForeignKey("employees.id"), nullable=False)
    division_id = db.Column(db.String(36), ForeignKey("divisions.id"), nullable=False)

    role = db.Column(db.String(50), nullable=False)   # ex: opérateur, superviseur, directeur
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)

    # --- Relations ---
    employee = db.relationship("Employee", backref=db.backref("division_assignments", lazy=True))
    division = db.relationship("Division", backref=db.backref("employees", lazy=True))

    def __repr__(self):
        return f"<DivisionEmployee emp={self.employee_id}, div={self.division_id}, role={self.role}>"