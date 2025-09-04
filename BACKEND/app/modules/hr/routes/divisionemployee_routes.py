# BACKEND\app\modules\hr\routes\divisionemployee_routes.py

from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

from app.modules.hr.schemas.division_employee.DivisionEmployeeCreateSchema import DivisionEmployeeCreateSchema
from app.modules.hr.schemas.division_employee.DivisionEmployeeSchema import DivisionEmployeeSchema
from app.modules.hr.schemas.division_employee.DivisionEmployeeUpdateSchema import DivisionEmployeeUpdateSchema

from app.modules.hr.services.divisionsemployees_service import update_division_employee_service,create_division_employee_service, list_division_employee
from app.common.response.response import success_response, error_response

divisionemployee_bp = Blueprint("divisionemployee", __name__, url_prefix="/divisionsemployees")

@divisionemployee_bp.route("/divisionemployee", methods=["POST"])
def create_divisionemployee():

    data = request.get_json()
    if not data:
        return error_response("Aucune donnée fournie", 400)

    try:
        schema = DivisionEmployeeCreateSchema()
        validated_obj = schema.load(data)  # -> DivisionEmployee
        division_employee_obj = create_division_employee_service(validated_obj)
        result = DivisionEmployeeSchema().dump(division_employee_obj)

        return success_response(
            data=result,
            message="Affectation employé/division créée avec succès"
        )

    except ValidationError as e:
        return error_response(
            "Erreur de validation",
            status_code=400,
            data=e.messages
        )
    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la création de l'affectation",
            status_code=500,
            data=str(e)
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )
    
@divisionemployee_bp.route("/divisionemployee", methods=["GET"])
def read_employee_affectation():
    employee_id = request.args.get('employee_id')

    try:
        divisionemployee = list_division_employee(employee_id)
        schema = DivisionEmployeeSchema(many = True)
        if not divisionemployee:
            return error_response("Aucune affectation trouvée", 404)
        return success_response(
            data=schema.dump(divisionemployee),
            message="Liste des divisions récupérée avec succès"
        )

    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la récupération des divisions",
            status_code=500,
            data=str(e)
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )


@divisionemployee_bp.route("/divisionemployee", methods=["PATCH"])
def update_divisionemployee():
    division_employee_id = request.args.get("divisionemployee_id")
    if not division_employee_id:
        return error_response("Paramètre 'divisionemployee_id' manquant", 400)

    data = request.get_json()
    if not data:
        return error_response("Aucune donnée fournie", 400)

    try:
        # Validation des données entrantes
        validated_data = DivisionEmployeeUpdateSchema().load(data, partial=True)

        # Appel du service pour mettre à jour
        updated_obj = update_division_employee_service(division_employee_id, validated_data)

        # Sérialisation pour la réponse
        result = DivisionEmployeeSchema().dump(updated_obj)

        return success_response(
            data=result,
            message="Affectation employé/division mise à jour avec succès"
        )

    except ValidationError as e:
        return error_response(
            "Erreur de validation",
            status_code=400,
            data=e.messages
        )
    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la mise à jour",
            status_code=500,
            data=str(e)
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )
