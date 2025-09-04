# BACKEND/app/modules/machine/routes/machine_routes.py

from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError

from app.modules.machine.services.machine_service import get_all_machines, update_machine_service, create_machine_service

from app.modules.machine.models.machine import Machine
from app.modules.machine.schemas.machine.MachineSchema import MachineSchema
from app.modules.machine.schemas.machine.MachineUpdateSchema import MachineUpdateSchema
from app.modules.machine.schemas.machine.MachineCreateSchema import MachineCreateSchema

from app.common.response.response import success_response, error_response

machine_bp = Blueprint("machines", __name__, url_prefix="/machines")


@machine_bp.route("/machines", methods=["GET"])
def list_machines():
    """Récupère la liste des machines avec filtres et tri."""
    machine_type = request.args.get("type")  # ex: ?type=capteur
    sort = request.args.get("sort")          # ex: ?sort=name

    try:
        machines = get_all_machines(machine_type=machine_type, sort=sort)
        schema = MachineSchema(many=True)

        if not machines:
            return error_response("Aucune machine trouvée", 404)

        return success_response(
            data=schema.dump(machines),
            message="Liste des machines récupérée avec succès"
        )

    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la récupération des machines",
            status_code=500,
            data=str(e)
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )

@machine_bp.route("/machine", methods=["PATCH"])
def update_machine():
    machine_id = request.args.get("machine_id")
    if not machine_id:
        return error_response("Paramètre 'machine_id' manquant", 400)

    data = request.get_json()
    if not data:
        return error_response("Aucune donnée fournie", 400)

    try:
    
        validated_data = MachineUpdateSchema().load(data, partial=True)
        updated_machine = update_machine_service(machine_id, validated_data)

        if not updated_machine:
            return error_response("Machine introuvable", 404)

        return success_response(
            data=MachineSchema().dump(updated_machine),
            message="Machine mise à jour avec succès"
        )

    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la mise à jour de la machine",
            status_code=500,
            data=str(e)
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )

@machine_bp.route("/machine", methods=["POST"])
def create_machine():
    data = request.get_json()

    if not data:
        return error_response("Aucune donnée reçue", 400)

    try:
        # Validation des données via le schéma
        validated_data = MachineCreateSchema().load(data)

        # Appel au service
        created_machine = create_machine_service(validated_data)

        if not created_machine:
            return error_response("Erreur lors de la création de la machine", 500)

        return success_response(
            data=MachineSchema().dump(created_machine),
            message="machine créée avec succès"
        )

    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la création de la machine",
            status_code=500,
            data=str(e)
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )
