# BACKEND/app/modules/hr/services/division_employee_service.py
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from app.core.extensions import db
from app.modules.hr.models.division_employee import DivisionEmployee
from app.modules.hr.models.employee import Employee




def create_division_employee_service(division_employee_obj: DivisionEmployee) -> DivisionEmployee:
    # contrôle de cohérence : l'employee est-il toujours en poste ?

    employee = Employee.query.filter_by(id=division_employee_obj.employee_id).first()

    if not employee:
        raise ValidationError({"employee_id": ["Employé inexistant."]})

    if employee.termination_date:
        raise ValidationError({"employee_id": ["L'employé n'est plus en poste."]})

    db.session.add(division_employee_obj)
    db.session.commit()
    return division_employee_obj


def update_division_employee_service(division_employee_id: str, data: dict) -> DivisionEmployee:
    """
    Met à jour une affectation DivisionEmployee existante.

    :param division_employee_id: ID de l'affectation
    :param data: dict validé par DivisionEmployeeUpdateSchema
    :return: instance mise à jour de DivisionEmployee
    """
    # Récupérer l'affectation
    division_employee_obj = DivisionEmployee.query.get(division_employee_id)
    if not division_employee_obj:
        raise ValidationError({"division_employee_id": ["Aucune affectation trouvée pour cet ID."]})

    # Met à jour seulement les attributs existants
    for key, value in data.items():
        if hasattr(division_employee_obj, key):
            setattr(division_employee_obj, key, value)

    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e

    return division_employee_obj

def list_division_employee(employee_id):
    query = DivisionEmployee.query
    
    if employee_id:
        query = query.filter_by(employee_id=employee_id)
    
    return query.all()