""" BACKEND\app\common\helper\mrp.py """

def explode_ingredients_recursive(article, quantity_needed, accumulated_needs, is_top_level=False):
    """
    Calcule récursivement les besoins en matières.
    
    :param article: L'article courant
    :param quantity_needed: La quantité requise
    :param accumulated_needs: Le dictionnaire accumulateur
    :param is_top_level: True si c'est l'article de l'OF (qu'on ne doit pas lister comme besoin)
    """
    
    recipe = article.active_recipe  # Votre helper property

    # -----------------------------------------------------------
    # ÉTAPE 1 : Enregistrer le besoin (Sauf si c'est le produit fini lui-même)
    # -----------------------------------------------------------
    if not is_top_level:
        code = article.code
        if code not in accumulated_needs:
            accumulated_needs[code] = {
                "code": code,
                "designation": article.designation,
                "unit": article.unite_code or "N/A",
                "quantity": 0.0,
                # Distinction utile pour l'affichage (Semi-Fini vs Matière Première)
                "type": "semi-fini" if recipe else "ingredient"
            }
        accumulated_needs[code]["quantity"] += quantity_needed

    # -----------------------------------------------------------
    # ÉTAPE 2 : Condition d'arrêt (Matière Première)
    # -----------------------------------------------------------
    if not recipe:
        return  # Pas d'enfants à explorer

    # -----------------------------------------------------------
    # ÉTAPE 3 : Récursion (Explosion de la recette)
    # -----------------------------------------------------------
    ref_size = float(recipe.taille_lot_ref)
    ratio = quantity_needed / ref_size if ref_size > 0 else 0

    for ingredient in recipe.ingredients:
        # Calcul quantité enfant
        qty_child = float(ingredient.quantity) * ratio if ingredient.is_proportional else float(ingredient.quantity)
        
        # Appel récursif
        # IMPORTANT : Les enfants ne sont jamais "top_level", on veut toujours les lister
        explode_ingredients_recursive(
            article=ingredient.article, 
            quantity_needed=qty_child, 
            accumulated_needs=accumulated_needs,
            is_top_level=False 
        )

def build_production_tree(article, quantity_needed):
    """
    Construit un arbre hiérarchique des besoins (Article -> Base -> MP).
    """
    recipe = article.active_recipe  # Votre helper property

    # 1. Création du Nœud courant
    node = {
        "code": article.code,
        "designation": article.designation,
        "quantity": round(quantity_needed, 4),
        "unit": article.unite_code or "N/A",
        "type": "semi-fini" if recipe else "ingredient"
    }

    # 2. Condition d'arrêt : Si c'est une MP (pas de recette), on renvoie le nœud tel quel
    if not recipe:
        return node

    # 3. Récursion : On calcule les enfants
    node["composition"] = [] # La fameuse "sous-clef" demandée
    
    ref_size = float(recipe.taille_lot_ref)
    ratio = quantity_needed / ref_size if ref_size > 0 else 0

    for ing in recipe.ingredients:
        # Calcul quantité enfant
        qty_child = float(ing.quantity) * ratio if ing.is_proportional else float(ing.quantity)
        
        # Appel récursif pour construire la branche de cet ingrédient
        child_node = build_production_tree(ing.article, qty_child)
        
        node["composition"].append(child_node)

    return node