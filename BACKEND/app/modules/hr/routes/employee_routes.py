# BACKEND\app\modules\hr\routes\employee_routes.py

from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

from app.modules.hr.services.employee_services import *

from app.modules.hr.schemas.employee.EmployeeCreateSchema import EmployeeCreateSchema
from app.modules.hr.schemas.employee.EmployeeSchema import EmployeeSchema
from app.modules.hr.schemas.employee.EmployeeUpdateSchema import EmployeeUpdateSchema

from app.common.response.response import success_response, error_response

employee_bp = Blueprint("employee", __name__, url_prefix="/employees")

@employee_bp.route("/employees", methods=["GET"])
def list_employees():
    """Récupère la liste des employés avec tri optionnel."""
    sort = request.args.get("sort")  # ex: ?sort=last_name ou ?sort=hire_date

    try:
        employees = get_all_employees(sort=sort)  # Note le pluriel pour la cohérence
        schema = EmployeeSchema(many=True)

        if not employees:
            return error_response("Aucun employé trouvé", 404)

        return success_response(
            data=schema.dump(employees),
            message="Liste des employés récupérée avec succès"
        )

    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la récupération des employés",
            status_code=500,
            data=str(e)
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )

@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    """Crée un nouvel employé."""
    data = request.get_json()

    if not data:
        return error_response("Aucune donnée fournie", 400)

    try:
        # Validation des données via le schema
        validated_data = EmployeeCreateSchema().load(data)

        # Création via le service
        created_employee = create_employee_service(validated_data)

        if not created_employee:
            return error_response("Erreur lors de la création de l'employé", 500)

        # Retourne l'objet créé
        return success_response(
            data=EmployeeSchema().dump(created_employee),
            message="Employé créé avec succès"
        )

    except ValidationError as ve:
        return error_response(
            "Données invalides",
            status_code=400,
            data=ve.messages
        )
    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la création de l'employé",
            status_code=500,
            data=str(e)
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )


@employee_bp.route("/employee", methods=["PATCH"])
def update_employee():
    """Met à jour un employé existant."""
    employee_id = request.args.get("employee_id")
    if not employee_id:
        return error_response("Paramètre 'employee_id' manquant", 400)

    data = request.get_json()
    if not data:
        return error_response("Aucune donnée fournie", 400)

    try:
        # Validation partielle
        validated_data = EmployeeUpdateSchema().load(data, partial=True)

        # Mise à jour via le service
        updated_employee = update_employee_service(employee_id, validated_data)

        if not updated_employee:
            return error_response("Employé introuvable", 404)

        return success_response(
            data=EmployeeSchema().dump(updated_employee),
            message="Employé mis à jour avec succès"
        )

    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la mise à jour de l'employé",
            status_code=500,
            data=str(e)
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )