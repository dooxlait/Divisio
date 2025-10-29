from flask import Blueprint
from app.modules.articles.services import get_all_fournisseurs
from app.common.response.response import success_response, error_response
from app.modules.articles.schemas.fournisseur import FournisseurSchema

fournisseur_bp = Blueprint('fournisseur_bp', __name__, url_prefix='/fournisseurs')

@fournisseur_bp.route('/', methods=['GET'])
def get_fournisseurs():
    schema = FournisseurSchema(many=True)
    try:
        fournisseurs = get_all_fournisseurs()
        result = schema.dump(fournisseurs)
        return success_response(data=result, message="Fournisseurs retrieved successfully")
    except Exception as e:
        return error_response(message=str(e), status_code=500)
    