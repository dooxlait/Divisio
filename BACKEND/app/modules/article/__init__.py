from app.modules.article.routes import articletype_bp

def register_article_routes(app, url_prefix="/articles"):
    app.register_blueprint(articletype_bp, url_prefix=url_prefix)


