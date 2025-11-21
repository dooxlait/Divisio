# BACKEND\app\modules\production\services\recette_ingredient_service.py

from app.core.extensions import db
from app.modules.articles.models import Article, Unite
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

    # Nettoyage initial du dataframe
    df = df.dropna(how="all")
    df.columns = df.columns.str.strip()

    new_created = 0
    failed_rows = []

    for index, row in df.iterrows():
        try:
            # Extraction sécurisée
            recette_code = row.get("recipe_code")
            ingredient_code = row.get("ingredient_code")
            quantite = row.get("quantity", 0)
            unite_code = row.get("unite")
            is_proportional = row.get("is_proportional", True)

            # Vérifications
            if not recette_code:
                raise ValueError("Le code recette (recipe_code) est obligatoire.")
            if not ingredient_code:
                raise ValueError("Le code ingrédient (ingredient_code) est obligatoire.")
            if quantite is None or quantite <= 0:
                raise ValueError("La quantité doit être supérieure à zéro.")
            if not unite_code:
                raise ValueError("Le code unité (unite) est obligatoire.")

            # Recherche des objets
            recipe = read_recipe(filters={"code": recette_code})
            if not recipe:
                raise ValueError(f"Recette code '{recette_code}' introuvable.")

            article = lire_articles_filter(filters={"code": ingredient_code})
            if not article:
                raise ValueError(f"Article ingredient code '{ingredient_code}' introuvable.")

            unite = Unite.query.filter_by(code=unite_code).first()
            if not unite:
                raise ValueError(f"Unité code '{unite_code}' introuvable.")

            data = {
                "recipe_id": recipe.id,
                "article_id": article.id,
                "unite_id": unite.id,
                "quantity": quantite,
                "is_proportional": is_proportional,
            }

            # Création sans commit
            create_ingredient_recipe(**data)
            new_created += 1

        except Exception as e:
            failed_rows.append({
                "row_index": index,
                "row_data": row.to_dict(),
                "error": str(e)
            })

    # Commit global
    try:
        if new_created > 0:
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        return 0, [{
            "error": f"Erreur lors du commit en base : {str(e)}"
        }]

    return new_created, failed_rows
