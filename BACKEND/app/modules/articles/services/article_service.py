import pandas as pd
from marshmallow import ValidationError
from app.core.extensions import db
from app.modules.articles.models import Article
from app.modules.articles.schemas.article.article_schema import ArticleSchema

article_schema = ArticleSchema()

def lire_excel(fichier):
    """Lit le fichier Excel et renvoie un DataFrame."""
    try:
        return pd.read_excel(fichier)
    except Exception as e:
        raise ValueError(f"Erreur lors de la lecture du fichier Excel : {str(e)}")

def convertir_en_articles(df):
    """Convertit un DataFrame en objets Article après validation via ArticleSchema."""
    articles = []
    for _, row in df.iterrows():
        try:
            data = {
                "code": row["code"],
                "designation": row["designation"],
                "ean": row.get("ean"),
                "is_active": row.get("is_active", True),
                "id_categorie": row.get("id_categorie"),
                "id_unite": row.get("id_unite"),
            }
            article = article_schema.load(data)
            articles.append(article)
        except ValidationError as err:
            raise ValueError(f"Erreur de validation sur la ligne {_} : {err.messages}")
    return articles

def enregistrer_articles(articles):
    """Ajoute les objets Article en base et valide la transaction."""
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
