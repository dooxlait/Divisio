from flask import Blueprint, request, send_file
from datetime import datetime
import os

from app.common.response.response import success_response, error_response
from app.modules.articles.services import create_article_by_list, lire_articles, export_to_excel
from app.modules.articles.schemas.article import ArticleSchema
from app.core.config import Config

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
    

@article_bp.route("/export", methods=["GET"])
def export_articles():
    try:
        articles = lire_articles()
        schema = ArticleSchema(many=True)
        articles_data = schema.dump(articles)

        export_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", Config.EXPORT_DIR))
        os.makedirs(export_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(export_dir, f"exported_articles_{timestamp}.xlsx")

        export_to_excel(articles_data, output_file)

        # Envoi du fichier au client
        return send_file(
            output_file,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            as_attachment=True,
            download_name=f"exported_articles_{timestamp}.xlsx"
        )
    except Exception as e:
        return error_response(f"Erreur lors de l'exportation : {str(e)}", 500)
    
@article_bp.route("/", methods=["GET"])
def get_articles():
    articles = lire_articles()
    schema = ArticleSchema(many=True)
    articles = schema.dump(articles)
    return success_response(
        data={"articles": articles},
        message="Articles récupérés avec succès",
        status_code=200
    )