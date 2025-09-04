# BACKEND\app\modules\factory\routes\site_routes.py

from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError

from app.modules.factory.services import get_all_sites, create_site_service
from app.modules.factory.schemas.site import SiteSchema
from app.modules.factory.schemas.site.SiteCreateSchema import SiteCreateSchema
from app.common.response.response import success_response, error_response

site_bp = Blueprint("site", __name__, url_prefix="/sites")

@site_bp.route("/sites", methods=["GET"])
def list_sites():
    try:
        sites = get_all_sites()
        schema = SiteSchema(many=True)

        if not sites:
            return error_response("Aucun site trouvé", 404)

        return success_response(
            data=schema.dump(sites),
            message="Liste des sites récupérée avec succès"
        )

    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la récupération des sites",
            status_code=500,
            data=str(e)
        )

    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )
    
@site_bp.route("/sites", methods=["POST"])
def create_site():
    data = request.get_json()

    if not data:
        return error_response("Aucune donnée reçue", 400)

    try:
        # Validation des données via le schéma
        validated_data = SiteCreateSchema().load(data)

        # Appel au service
        created_site = create_site_service(validated_data)

        if not created_site:
            return error_response("Erreur lors de la création de la site", 500)

        return success_response(
            data=SiteSchema().dump(created_site),
            message="site créée avec succès"
        )

    except SQLAlchemyError as e:
        return error_response(
            "Erreur lors de la création du site",
            status_code=500,
            data=str(e)
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )
    