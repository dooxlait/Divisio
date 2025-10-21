# BACKEND\app\modules\articles\__init__.py
from .routes import category_bp
from .routes import article_bp

def register_article_routes(app, url_prefix="/articles"):
    app.register_blueprint(category_bp, url_prefix=url_prefix)
    app.register_blueprint(article_bp, url_prefix=url_prefix)