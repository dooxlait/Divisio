from app.modules.article.models import ArticleType
from app.core.extensions import db

def readallarticletype():
    result = ArticleType.query.all()
    return result

def writearticletype(articletype):
    try:
        db.session.add(articletype)
        db.session.commit()
        return articletype
    except Exception as e:
        db.session.rollback()
        print(f"[ERREUR] Échec création de l'article type: {e}")
        return None