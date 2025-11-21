# BACKEND\app\modules\production\services\recette_ingredient_service.py

from app.core.extensions import db
from app.modules.articles.models import Article
from app.modules.production.models.recette_ingredient  import RecetteIngredient
from app.modules.production.services.production_recipe_service import read_recipe
from app.modules.articles.services.article_service  import lire_articles_filter


def create_ingredient_recipe(**data):
    """
    Crée une instance de recette et l'ajoute à la session.
    NE COMMIT PAS (pour permettre le bulk insert).
    """
    new_ingredient_recipe = RecetteIngredient(**data)
    db.session.add(new_ingredient_recipe)
    return new_ingredient_recipe

def create_ingredient_recipe_by_list(df):
    # Initialisation
    new_created = 0
    failed_rows = []

    for index, row in df.iterrows():
        try:
            # Initialisation
            new_created = 0
            failed_rows = []
            
            # Nettoyage
            df = df.dropna(how="all")
            df.columns = df.columns.str.strip()
            
            # Parcours des lignes
            for index, row in df.iterrows():
                try:
                    # Extraction sécurisée (évite les KeyErrors si une colonne manque)
                    recette_code = row.get("recette_code")
                    ingredient_code = row.get("ingredient_code", "")
                    quantite = row.get("quantite", 0)
                    unite_code = row.get("unite", "")
                    is_proportional = data.get("is_proportional", True)

                    if not recette_code:
                        raise ValueError("Le code recette (recette_code) est obligatoire.")
                    if not ingredient_code:
                        raise ValueError("Le code ingrédient (ingredient_code) est obligatoire.")
                    if quantite <= 0:
                        raise ValueError("La quantité doit être supérieure à zéro.")

                    # recherche de recipe_id
                    recipe = read_recipe(filters={"code": recette_code})
                    if not recipe:
                        raise ValueError(f"Recette code '{recette_code}' introuvable.")
                    
                    article = lire_articles_filter(filters={"code": ingredient_code})
                    if not article:
                        raise ValueError(f"Article ingredient code '{ingredient_code}' introuvable.")
                    
                    unite = Article.query.filter_by(code=unite_code).first()
                    if not unite:
                        raise ValueError(f"Unité code '{unite_code}' introuvable.")

                    data = {
                        "recipe_id": recipe.id,
                        "article_id": article.id,
                        "unite_id": unite.id,
                        "quantite": quantite,
                        "is_proportional": is_proportional,
                    }

                    # Ajout à la session (sans commit)
                    create_ingredient_recipe(**data)
                    new_created += 1
                except Exception as e:
                    # En cas d'erreur sur une ligne, on l'ajoute aux échecs
                    # Note: SQLAlchemy peut rollback automatiquement en cas d'erreur fatale au commit
                    failed_rows.append({
                        "row_index": index,
                        "row_data": str(row.to_dict()), # Utile pour le debug
                        "error": str(e)
                    })

        except Exception as e:
            failed_rows.append((index + 2, str(e)))  # +2 pour compenser l'index et l'en-tête

    return new_created, failed_rows