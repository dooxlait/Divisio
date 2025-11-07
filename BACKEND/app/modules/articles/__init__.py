# BACKEND\app\modules\articles\__init__.py
from .routes import category_bp
from .routes import article_bp
from .routes import marque_bp
from .routes import fournisseur_bp
from .routes import stock_bp
from .routes import article_composition_bp
from .routes import mouvement_stock_bp

def register_article_routes(app, url_prefix="/article"):
    app.register_blueprint(article_bp, url_prefix=f"{url_prefix}/articles")
    app.register_blueprint(marque_bp, url_prefix=f"{url_prefix}/marques")
    app.register_blueprint(category_bp, url_prefix=f"{url_prefix}/categories")
    app.register_blueprint(fournisseur_bp, url_prefix=f"{url_prefix}/fournisseurs")
    app.register_blueprint(stock_bp, url_prefix=f"{url_prefix}/stocks")
    app.register_blueprint(article_composition_bp, url_prefix=f"{url_prefix}/article-compositions")
    app.register_blueprint(mouvement_stock_bp, url_prefix=f"{url_prefix}/mouvement-stocks")