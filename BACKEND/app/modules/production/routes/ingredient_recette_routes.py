""" BACKEND\app\modules\production\routes\ingredient_recette_routes.py"""

from flask import Blueprint, request

from app.common.helper.excel_helper import lire_excel
from app.common.helper.parse_helper import parse_filter_params

from app.common.response.response import success_response, error_response

from app.modules.production.services.recette_ingredient_service import create_ingredient_recipe_by_list

from app.modules.production.schemas import RecetteIngredientSchema

ingredient_recette_bp = Blueprint("ingredient_recette_bp", __name__,)

@ingredient_recette_bp.route('/ingredient_recettes', methods=['POST'])
def create_ingredient_recette():
    file = request.files.get('file')
    if not file:
        return error_response("No file provided", 400)
    
    try:
        # creation du DF à partir du fichier excel (supposant que lire_excel existe)
        df = lire_excel(file)
        if df is None:
            return error_response("Failed to read Excel file", 500)
            
        # Envoi du DF au service de création
        new_created, failed_rows = create_ingredient_recipe_by_list(df)
        
        return success_response({
            "message": f"{new_created} ingredient recipes created successfully",
            "failed_rows": failed_rows
        })
    except Exception as e:
        # Capture les erreurs globales non gérées
        return error_response(str(e), 500)