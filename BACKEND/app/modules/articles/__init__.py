# BACKEND\app\modules\articles\__init__.py
from .routes import category_bp
from .routes import article_bp
from .routes import marque_bp


def register_article_routes(app, url_prefix="/article"):
    app.register_blueprint(article_bp, url_prefix=f"{url_prefix}/articles")
    app.register_blueprint(marque_bp, url_prefix=f"{url_prefix}/marques")
    app.register_blueprint(category_bp, url_prefix=f"{url_prefix}/categories")