import pandas as pd
import math

from marshmallow import ValidationError
from app.core.extensions import db
from app.modules.articles.models import Article
from app.modules.articles.schemas.article.article_schema import ArticleSchema

article_schema = ArticleSchema()

def lire_excel(fichier):
    """Lit le fichier Excel et renvoie un DataFrame."""
    print('[INFO] Lecture du fichier Excel pour l\'importation des articles.')
    try:
        return pd.read_excel(fichier)
    except Exception as e:
        raise ValueError(f"Erreur lors de la lecture du fichier Excel : {str(e)}")


def convertir_en_articles(df):
    articles = []
    print('[INFO] Conversion des données Excel en objets Article.')

    df = df.dropna(how="all")

    for idx, row in df.iterrows():
        if pd.isna(row.get("code")) or pd.isna(row.get("designation")):
            print(f"[WARN] Ligne {idx} ignorée : code ou designation manquant.")
            continue

        # Conversion correcte de ean
        ean_value = row.get("ean")
        if pd.isna(ean_value) or (isinstance(ean_value, float) and math.isnan(ean_value)):
            ean_value = None
        elif isinstance(ean_value, float) and ean_value.is_integer():
            # supprimer le .0
            ean_value = str(int(ean_value))
        else:
            ean_value = str(ean_value)

        data = {
            "code": str(row["code"]),
            "designation": str(row["designation"]),
            "ean": ean_value,
            "is_active": row.get("is_active") if not pd.isna(row.get("is_active")) else True,
        }

        try:
            article = article_schema.load(data)
            articles.append(article)
        except ValidationError as err:
            print(f"[ERROR] Ligne {idx} invalide : {err.messages}")

    return articles

def enregistrer_articles(articles):
    """Ajoute les objets Article en base et valide la transaction."""
    print('[INFO] Enregistrement des articles en base de données.')
    try:
        db.session.add_all(articles)
        db.session.commit()
        return len(articles)
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erreur lors de l'insertion en base : {str(e)}")

def create_article_by_list(fichier):
    """Orchestre l'import Excel en lecture, validation et persistance."""
    df = lire_excel(fichier)
    articles = convertir_en_articles(df)
    return enregistrer_articles(articles)

def export_to_excel(articles_data, output_file):
    """Exporte une liste de dictionnaires vers un fichier Excel."""
    print(f'[INFO] Exportation des articles vers le fichier {output_file}')
    try:
        df = pd.DataFrame(articles_data)
        df.to_excel(output_file, index=False)
    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'exportation vers Excel : {str(e)}")

def lire_articles():
    """Lit tous les articles en base de données."""
    print('[INFO] Lecture de tous les articles en base de données.')
    try:
        articles = Article.query.all()
        return articles
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la lecture des articles : {str(e)}")