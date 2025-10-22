from flask import Blueprint, request
from app.common.response.response import success_response, error_response
from app.modules.articles.services import create_article_by_list

article_bp = Blueprint('article_bp', __name__, url_prefix='/articles')

@article_bp.route("/", methods=["POST"])
def create_article_by_list_route():
    fichier = request.files.get("file")
    if not fichier:
        return error_response("Aucun fichier fourni", 400)

    try:
        count = create_article_by_list(fichier)
        return success_response(
            data={"imported": count},
            message="Importation effectuée avec succès",
            status_code=201
        )
    except Exception as e:
        return error_response(f"Erreur lors de l'importation : {str(e)}", 500)