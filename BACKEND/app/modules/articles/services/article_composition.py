# Module: BACKEND/app/modules/articles/services/article_composition.py

from app.core.extensions import db
from app.modules.articles.models import Article, CaracteristiqueArticle
from app.common.helper import *

def create_article_composition(article_id: int, composition_data: dict) -> dict:
    """
    Create a new article composition.

    :param article_id: ID of the article to which the composition belongs.
    :param composition_data: Data for the new composition.
    :return: The created article composition as a dictionary.
    """
    # Implementation goes here
    pass

def update_article_composition(composition_id: int, composition_data: dict) -> dict:
    """
    Update an existing article composition.

    :param composition_id: ID of the composition to update.
    :param composition_data: Updated data for the composition.
    :return: The updated article composition as a dictionary.
    """
    # Implementation goes here
    pass

def get_articles_by_caracteristique(**kwargs):
    """
    Récupère les articles filtrés selon les attributs de CaracteristiqueArticle.
    
    Exemple d'utilisation :
        get_articles_by_caracteristique(conditionnement_a_chaud=True, pcb=5)
    """
    query = Article.query.join(Article.caracteristique)
    
    for attr, value in kwargs.items():
        column = getattr(CaracteristiqueArticle, attr, None)
        if column is not None:
            query = query.filter(column == value)
    
    return query.all()

def rajoute_dlc_dgr_aux_articles(df):
    """
    Met à jour les articles avec les valeurs DLC et DGR du DataFrame.
    Retourne le nombre de caractéristiques mises à jour.
    """
    updated_count = 0

    for _, row in df.iterrows():
        code_article = row['Référence']
        dlc = row.get('DLC')
        dgr = row.get('DGR')

        # Récupération de l'article
        article = Article.query.filter_by(code=code_article).first()
        if not article:
            continue  # Article non trouvé, on passe au suivant

        # Création ou mise à jour de la caractéristique
        # On peut vérifier si une caractéristique existe déjà pour éviter doublons
        carac = CaracteristiqueArticle.query.filter_by(article_id=article.id).first()
        if not carac:
            carac = CaracteristiqueArticle(article_id=article.id)

        # Mise à jour des champs
        carac.dlc = dlc
        carac.dgr = dgr

        # Ajout explicite à la session si ce n'est pas déjà fait
        if carac not in db.session:
            db.session.add(carac)

        # Ajout à la relation de l'article (optionnel, si la relation est définie)
        if carac not in article.caracteristique:
            article.caracteristique.append(carac)

        updated_count += 1

    # Commit de toutes les modifications
    db.session.commit()
    return updated_count
    
