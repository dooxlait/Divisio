from app.modules.article.routes import articletype_bp
from app.modules.article.routes import article_bp
from app.modules.article.routes import articlecomposition_bp

def register_article_routes(app, url_prefix="/articles"):
    app.register_blueprint(articletype_bp, url_prefix=url_prefix)
    app.register_blueprint(article_bp, url_prefix=url_prefix)
    app.register_blueprint(articlecomposition_bp, url_prefix=url_prefix)


