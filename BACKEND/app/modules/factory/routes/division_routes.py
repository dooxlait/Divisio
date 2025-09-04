# BACKEND\app\modules\factory\routes\division_routes.py

from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError

from app.modules.factory.schemas.division import DivisionCreateSchema, DivisionSchema, DivisionUpdateSchema
from app.modules.factory.services import get_all_divisions, update_division_service, create_division_service

from app.common.response.response import success_response, error_response

division_bp = Blueprint("division", __name__, url_prefix="/divisions")

@division_bp.route("/divisions", methods=["GET"])
def list_divisions():
    # Récupération des query params
    div_type = request.args.get("type")   # ex: ?type=atelier
    sort = request.args.get("sort")       # ex: ?sort=name

    try:
        divisions = get_all_divisions(div_type=div_type, sort=sort)  # on délègue la logique au service
        schema = DivisionSchema(many=True)

        if not divisions:
            return error_response("Aucune division trouvée", 404)

        return success_response(
            data=schema.dump(divisions),
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

@division_bp.route("/division", methods=["PATCH"])
def update_division():
    # Récupération de l'ID de la division dans les query params
    div_id = request.args.get("division_id")
    if not div_id:
        return error_response("Paramètre 'division_id' manquant", 400)

    data = request.get_json()

    try:
        # Validation partielle des données
        validated_data = DivisionUpdateSchema().load(data)

        # Appel au service
        updated_division = update_division_service(div_id, validated_data)

        if not updated_division:
            return error_response("Division introuvable", 404)

        return success_response(
            data=DivisionSchema().dump(updated_division),
            message="Division mise à jour avec succès"
        )

    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la mise à jour de la division",
            status_code=500,
            data=str(e)
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )
    

@division_bp.route("/division", methods=["POST"])
def create_division():
    data = request.get_json()

    if not data:
        return error_response("Aucune donnée reçue", 400)

    try:
        # Validation des données via le schéma
        validated_data = DivisionCreateSchema().load(data)

        # Appel au service
        created_division = create_division_service(validated_data)

        if not created_division:
            return error_response("Erreur lors de la création de la division", 500)

        return success_response(
            data=DivisionSchema().dump(created_division),
            message="Division créée avec succès"
        )

    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la création de la division",
            status_code=500,
            data=str(e)
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )