from app.modules.article.models import Article
from app.core.extensions import db

def getAllArticle():
    # Récupérer la liste de tous les articles
    result = Article.query.all()
    return result

def getArticleDetails(article_id):
    # Récupérer les détails d'un article
    result = Article.query.filter_by(id=article_id).first()
    return result

def createArticle(data):
    # Création d'un article
    try:
        db.session.add(data)
        db.session.commit()
        return data
    except Exception as e:
        db.session.rollback()
        print(f"[ERREUR] Échec création de l'article : {e}")
        return None


def updateArticle(data, article_id):
    # Modifier un article donné
    pass

def deleteArticle(article_id):
    # suppression d'un article
    pass