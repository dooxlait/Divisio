# BACKEND\app\modules\article\routes\article_routes.py

from flask import Blueprint
from app.modules.article.service.article_service import getAllArticle 
from app.common.response.response import success_response, error_response
from app.modules.article.schemas import ArticleSchema

article_bp = Blueprint('article', __name__, url_prefix="/article")

@article_bp.route('/articles', methods=["GET"])
def getAllArticle_route():
    articles = getAllArticle()
    schemas = ArticleSchema(many=True)
    if articles:
        return success_response(
            data=schemas.dump(articles),
            message="Liste des articles récupérée avec succès"
        )
    else:
        return error_response("Aucun article trouvé", 404)