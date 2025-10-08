# BACKEND\app\modules\article\routes\articletypes_routes.py

from flask import Blueprint, request
from app.modules.article.service.articletype_service import readallarticletype, writearticletype
from app.modules.article.schemas.articles_types import ArticleTypeCreateSchema
from app.common.response.response import success_response, error_response

articletype_bp = Blueprint('articletype', __name__, url_prefix="/articletype")

@articletype_bp.route("/articletype", methods=['GET'])
def getArticleType_route():
    articlestypes = readallarticletype()
    schemas = ArticleTypeCreateSchema(many=True)
    if articlestypes:
        return success_response(
            data=schemas.dump(articlestypes),
            message="Liste des types articles récupérée avec succès"
        )
    else:
        return error_response("Aucun article type trouvé", 404)


@articletype_bp.route('/articletype', methods=['POST'])
def readArticleType_route():
    data = request.get_json()

    if not data:
        return error_response("Aucune donnée reçue", 400)
    
    try:
        validated_schema = ArticleTypeCreateSchema().load(data)
        created_articletype = writearticletype(validated_schema)
        if not created_articletype:
            return error_response("Erreur lors de la création du type article", 500)

        return success_response(
            data=ArticleTypeCreateSchema().dump(created_articletype),
            message="article type créé avec succès"
        )
    except Exception as e:
        return error_response(
            "Erreur interne du serveur",
            status_code=500,
            data=str(e)
        )
