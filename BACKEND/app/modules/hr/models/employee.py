from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy import UniqueConstraint

class Employee(BaseModel):
    __tablename__ = "employees"
    __table_args__ = (
        UniqueConstraint('first_name', 'last_name', 'hire_date',name='uq_employee_name_hiredate'),
    )

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    matricule = db.Column(db.String(10), unique=True, nullable=False)

    hire_date = db.Column(db.Date, nullable=False)
    termination_date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"<Employee {self.first_name} {self.last_name} - {self.matricule}>"