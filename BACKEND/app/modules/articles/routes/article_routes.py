from flask import Blueprint

article_bp = Blueprint('article_bp', __name__, url_prefix='/articles')