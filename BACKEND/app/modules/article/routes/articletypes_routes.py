from flask import Blueprint, request
from app.modules.article.service import readallarticletype, writearticletype
from app.modules.article.schemas import articletype_schema_creation
from app.common.response.response import success_response, error_response

articletype_bp = Blueprint('articletype', __name__, url_prefix="/articletype")

@articletype_bp.routes("/articletype", methods=['GET'])
def getArticleType_route():
    articlestypes = readallarticletype()
    schemas = articletype_schema_creation(many=True)
    if articlestypes:
        return success_response(
            data=schemas.dump(articlestypes),
            message="Liste des types articles récupérée avec succès"
        )
    else:
        return error_response("Aucun site trouvé", 404)


@articletype_bp.routes('/articletype', methods=['POST'])
def readArticleType_route():
    data = request.get_json()

    if not data:
        return error_response("Aucune donnée reçue", 400)
    
    try:
        validated_schema = articletype_schema_creation().load(data)
        created_articletype = writearticletype(validated_schema)
        if not created_articletype:
            return error_response("Erreur lors de la création du type article", 500)

        return success_response(
            data=articletype_schema_creation().dump(created_articletype),
            message="article type créé avec succès"
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )
