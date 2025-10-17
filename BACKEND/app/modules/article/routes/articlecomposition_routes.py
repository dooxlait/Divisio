# BACKEND\app\modules\article\routes\articlecomposition_routes.py

from flask import Blueprint, request
from marshmallow import ValidationError

from app.modules.article.schemas.article_composition import ArticleCompositionSchema
from app.modules.article.service.articlecomposition_service import add_article_component
from app.common.response.response import success_response, error_response

articlecomposition_bp = Blueprint('articlecomposition', __name__, url_prefix="/articlecomposition")

@articlecomposition_bp.route('/articlecomposition', methods=['POST'])
def create_article_composition_route():
    """Créer une composition d'article."""
    try:
        data = request.get_json()
        schema = ArticleCompositionSchema()

        # Validation du payload
        validated_data = schema.load(data)

        # Création en base via service
        created_composition = add_article_component(validated_data)

        # Réponse succès
        return success_response(
            data=schema.dump(created_composition),
            message="Composition d'article créée avec succès",
            status_code=201
        )

    except ValidationError as err:
        # Erreurs de validation du schéma Marshmallow
        return error_response(err.messages, 400)

    except Exception as e:
        # Autres erreurs (ex: SQLAlchemy, contraintes, etc.)
        return error_response(
            f"Erreur lors de la création de la composition d'article : {str(e)}",
            500
        )


