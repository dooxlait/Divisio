# BACKEND\app\modules\article\routes\article_routes.py

from flask import Blueprint, request
from marshmallow import ValidationError
from app.modules.article.service.article_service import getAllArticle, getArticleDetails, createArticle
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

@article_bp.route('/article/<string:id>', methods=['GET'])
def getArticleDetails_routes(id):
    article = getArticleDetails(id)
    schema = ArticleSchema()
    if article:
        return success_response(
            data=schema.dump(article),
            message="Article récupéré avec succès"
        )
    else:
        return error_response("Aucun article trouvé", 404)

@article_bp.route('/article', methods=['POST'])
def create_article_route():
    try:
        data = request.get_json()  # ✅ plus clair que "article"
        schema = ArticleSchema()

        # ✅ Validation et désérialisation
        validated_article = schema.load(data)

        # ✅ Appel du service ou du modèle
        created_article = createArticle(validated_article)

        # ✅ Retour succès
        return success_response(
            data=schema.dump(created_article),
            message="Article créé avec succès",
            status_code=201
        )

    except ValidationError as err:
        # Erreurs de validation du schéma
        return error_response(err.messages, 400)

    except Exception as e:
        # Autres erreurs (ex: base de données)
        return error_response(
            f"Erreur lors de la création de l'article : {str(e)}",
            500
        )