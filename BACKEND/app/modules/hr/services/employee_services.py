# BACKEND\app\modules\hr\services\employee_services.py

from app.modules.hr.models.employee import Employee
from app.core.extensions import db

def get_all_employees(sort=None):
    query = Employee.query

    if sort:
        if sort == "name":
            query = query.order_by(Employee.last_name.asc())
        elif sort == "date":
            query = query.order_by(Employee.hire_date.asc())

    return query.all()

def update_employee_service(employee_id: str, data: dict):
    """Met à jour un employé existant."""
    employee_obj = Employee.query.get(employee_id)
    if not employee_obj:
        return None

    for key, value in data.items():
        if hasattr(employee_obj, key):
            setattr(employee_obj, key, value)

    db.session.commit()
    return employee_obj

def create_employee_service(employee):
    try:
        db.session.add(employee)
        db.session.commit()
        return employee
    except Exception as e:
        db.session.rollback()
        print(f"[ERREUR] Échec création employee: {e}")
        return None
