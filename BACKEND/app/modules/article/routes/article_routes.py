# BACKEND\app\modules\article\routes\article_routes.py

from flask import Blueprint

article_bp = Blueprint('article', __name__, url_prefix="/article")

@article_bp.route('/articles', methods=["GET"])
def getAllArticle_route():
    pass