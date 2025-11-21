# Module: BACKEND/app/modules/articles/services/article_composition.py

from typing import Dict, Any
from app.core.extensions import db
import pandas as pd

from app.modules.articles.models import Article, CaracteristiqueArticle
from app.common.helper import *  # Assurez-vous que ce module existe

# ==============================================================================
# FONCTIONS CRUD COMPOSITIONS (Placeholders)
# ==============================================================================

def create_article_composition(article_id: int, composition_data: dict) -> dict:
    """
    Create a new article composition.
    """
    # Implementation goes here
    pass

def update_article_composition(composition_id: int, composition_data: dict) -> dict:
    """
    Update an existing article composition.
    """
    # Implementation goes here
    pass

# ==============================================================================
# FONCTIONS DE RECHERCHE
# ==============================================================================

def get_articles_by_caracteristique(**kwargs):
    """
    Récupère les articles filtrés selon les attributs de CaracteristiqueArticle.
    
    Exemple : get_articles_by_caracteristique(conditionnement_a_chaud=True, pcb=5)
    """
    query = Article.query.join(Article.caracteristique)
    
    for attr, value in kwargs.items():
        # Vérifie si l'attribut existe dans le modèle pour éviter les erreurs SQL
        column = getattr(CaracteristiqueArticle, attr, None)
        if column is not None:
            query = query.filter(column == value)
    
    return query.all()

# ==============================================================================
# FONCTIONS D'IMPORT ET MISE À JOUR (FACTORISÉES)
# ==============================================================================

def _update_caracteristiques_from_df(df: pd.DataFrame, mapping_col_attr: Dict[str, str]) -> int:
    """
    Fonction helper générique pour mettre à jour CaracteristiqueArticle depuis un DataFrame.
    
    :param df: Le DataFrame source.
    :param mapping_col_attr: Dict { 'NomColonneExcel': 'nom_attribut_modele' }
    :return: Nombre d'articles mis à jour.
    """
    updated_count = 0

    for _, row in df.iterrows():
        # Récupération du code article (clé de liaison)
        code_article = row.get('Référence')
        if not code_article:
            continue

        # Recherche de l'article
        article = Article.query.filter_by(code=str(code_article)).first()
        if not article:
            continue

        # Gestion de la relation One-to-One (Get or Create)
        carac = article.caracteristique
        if not carac:
            carac = CaracteristiqueArticle(id_article=article.id)
            db.session.add(carac)

        # Mise à jour dynamique des champs basés sur le mapping
        for col_excel, attr_model in mapping_col_attr.items():
            val = row.get(col_excel)
            # Conversion des NaN Pandas en None pour SQL
            if pd.isna(val):
                val = None
            
            # Mise à jour de l'attribut sur l'objet SQLAlchemy
            if hasattr(CaracteristiqueArticle, attr_model):
                setattr(carac, attr_model, val)

        updated_count += 1

    # Commit unique à la fin du traitement
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"[ERREUR SQL] Lors de la mise à jour des caractéristiques : {str(e)}")
        return 0

    return updated_count


def rajoute_dlc_dgr_aux_articles(df: pd.DataFrame) -> int:
    """
    Met à jour les articles avec les valeurs DLC et DGR du DataFrame.
    """
    mapping = {
        'DLC': 'DLC',
        'DGR': 'DGR'
    }
    return _update_caracteristiques_from_df(df, mapping)


def rajouter_infos_etiquettes_colis_aux_articles(df: pd.DataFrame) -> int:
    """
    Met à jour l'information d'étiquetage colis.
    """
    mapping = {
        'etiquette_sur_chaque_colis': 'etiquette_sur_chaque_colis'
    }
    return _update_caracteristiques_from_df(df, mapping)


def rajouter_gamme_aux_articles(df: pd.DataFrame) -> int:
    """
    Met à jour la gamme des articles.
    """
    mapping = {
        'Gamme': 'gamme'
    }
    return _update_caracteristiques_from_df(df, mapping)