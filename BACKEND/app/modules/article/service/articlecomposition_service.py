# BACKEND\app\modules\article\service\articlecomposition_service.py

from app.modules.article.models import ArticleComposition, Article
from app.core.extensions import db

def add_article_component(parent_id, composant_id, quantite):
    # Vérifie que les deux articles existent
    parent = Article.query.filter_by(id=parent_id).first()
    composant = Article.query.filter_by(id=composant_id).first()
    if not (parent and composant):
        return None

    # Vérifie qu’il n’existe pas déjà de lien (parent_id, composant_id)
    lien = ArticleComposition.query.filter_by(
        parent_article_id=parent_id,
        composant_article_id=composant_id
    ).first()
    if lien:
        return None

    # Crée et ajoute la nouvelle composition
    new_composition = ArticleComposition(
        parent_article_id=parent_id,
        composant_article_id=composant_id,
        quantite=quantite
    )
    db.session.add(new_composition)
    db.session.commit()
    return new_composition
    


def get_article_composition(parent_id):
    # Liste les composants d’un article parent.
    
    pass

def get_articles_using_component(composant_id):
    # Liste les parents qui utilisent cet article.
    pass

def update_article_component(parent_id, composant_id, quantite):
    # Met à jour la quantité utilisée.
    pass
    
def delete_article_component(parent_id, composant_id):
    # Supprime la relation entre deux articles.
    pass