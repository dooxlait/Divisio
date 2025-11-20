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
        get_articles_by_caracteristique(<url>?conditionnement_a_chaud=True, pcb=5)
    """
    query = Article.query.join(Article.caracteristique)
    
    for attr, value in kwargs.items():
        column = getattr(CaracteristiqueArticle, attr, None)
        if column is not None:
            query = query.filter(column == value)
    
    return query.all()

def rajouter_gamme_aux_articles(df):
    updated_count = 0
    errors = []

    for _, row in df.iterrows():
        code_article = row['Référence']
        gamme = row.get('Gamme')

        article = Article.query.filter_by(code=code_article).first()
        if not article:
            continue

        # 1. Vérifier si une caractéristique existe déjà
        carac = article.caracteristique

        # 2. Si elle n'existe pas, en créer une
        if not carac:
            carac = CaracteristiqueArticle(id_article=article.id)
            db.session.add(carac)

        # 3. Mettre à jour la gamme
        carac.gamme = gamme

        updated_count += 1

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        errors.append(str(e))

    return updated_count

def rajoute_dlc_dgr_aux_articles(df):
    """
    Met à jour les articles avec les valeurs DLC et DGR du DataFrame.
    Retourne le nombre de caractéristiques mises à jour et les erreurs éventuelles.
    """
    updated_count = 0
    errors = []

    for _, row in df.iterrows():
        code_article = row['Référence']
        dlc = row.get('DLC')
        dgr = row.get('DGR')

        article = Article.query.filter_by(code=code_article).first()
        if not article:
            continue

        carac = CaracteristiqueArticle.query.filter_by(id_article=article.id).first()
        if not carac:
            carac = CaracteristiqueArticle(id_article=article.id)

        carac.DLC = dlc
        carac.DGR = dgr

        if carac not in db.session:
            db.session.add(carac)

        if hasattr(article.caracteristique, 'append'):
            if carac not in article.caracteristique:
                article.caracteristique.append(carac)

        updated_count += 1

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        errors.append(str(e))

    return updated_count

    
