from marshmallow import fields, post_dump
from app.common.base.base_schema import BaseSchema
from app.modules.production.models.recette_ingredient import RecetteIngredient
from app.modules.production.models.production_recipe import ProductionRecipe
from app.modules.production.schemas.recette_ingredient import RecetteIngredientSchema
from sqlalchemy.orm import joinedload

class ProductionRecipeSchema(BaseSchema):
    ingredients = fields.Nested(RecetteIngredientSchema, many=True)

    class Meta:
        model = ProductionRecipe
        load_instance = True
        include_fk = True

    @post_dump(pass_many=False)
    def expand_subrecipes(self, data, **kwargs):
        """
        Ajoute les sous-recettes ET recalcule les quantités proportionnellement.
        """
        # Set local pour éviter la récursion infinie dans cette branche
        visited = set() 

        def _expand(ingredients_list, parent_ratio=1.0):
            for ingredient in ingredients_list:
                article_id = ingredient.get('article_id')
                
                # Quantité demandée par la recette parente pour cet ingrédient
                qty_needed = float(ingredient.get('quantity', 0))

                if not article_id:
                    continue

                if article_id in visited:
                    continue
                
                # On marque comme visité pour éviter les boucles A -> B -> A
                # Note : Dans une structure d'arbre complexe, il faudrait gérer le visited par branche
                visited.add(article_id)

                # Recherche de la sous-recette
                sub_recipe = (
                    ProductionRecipe.query
                    .options(
                        joinedload(ProductionRecipe.ingredients)
                        .joinedload(RecetteIngredient.article),
                        joinedload(ProductionRecipe.ingredients)
                        .joinedload(RecetteIngredient.unite)
                    )
                    .filter_by(article_output_id=article_id)
                    .first()
                )

                if sub_recipe:
                    # 1. On dump la recette brute (celle de ref, ex: 1000L)
                    sub_recipe_data = ProductionRecipeSchema().dump(sub_recipe)
                    
                    # 2. On calcule le ratio
                    # Ex: J'ai besoin de 940L, la recette de ref fait 1000L. Ratio = 0.94
                    ref_qty = float(sub_recipe.taille_lot_ref)
                    ratio = (qty_needed / ref_qty) if ref_qty > 0 else 0

                    # 3. On met à jour les infos de la sous-recette pour l'affichage
                    # On indique que cette "version" de la recette est pour 940L
                    sub_recipe_data['taille_lot_ref'] = f"{qty_needed:.4f}" 

                    # 4. On recalcule tous les ingrédients de la sous-recette
                    for sub_ing in sub_recipe_data.get('ingredients', []):
                        if sub_ing.get('is_proportional', True):
                            original_qty = float(sub_ing['quantity'])
                            new_qty = original_qty * ratio
                            sub_ing['quantity'] = f"{new_qty:.4f}"

                    # 5. On attache la sous-recette recalculée
                    ingredient['subrecipe'] = sub_recipe_data

                    # 6. Récursion : On descend dans les enfants avec le nouveau contexte si besoin
                    # (Ici on repasse simplement la liste des ingrédients recalculés)
                    _expand(ingredient['subrecipe'].get('ingredients', []))

        _expand(data.get('ingredients', []))
        return data