from flask import Blueprint, request

from app.common.helper.excel_helper import lire_excel
from app.common.helper.parse_helper import parse_filter_params

from app.common.response.response import success_response, error_response

from app.modules.production.services.production_recipe_service import create_recipe_by_list, read_recipe

from app.modules.production.schemas import ProductionRecipeSchema

production_recipe_bp = Blueprint('production_recipe', __name__)

@production_recipe_bp.route('/production_recipes', methods=['POST'])
def create_production_recipe():
    file = request.files.get('file')
    if not file:
        return error_response("No file provided", 400)
    
    try:
        # creation du DF à partir du fichier excel (supposant que lire_excel existe)
        df = lire_excel(file)
        if df is None:
            return error_response("Failed to read Excel file", 500)
            
        # Envoi du DF au service de création
        new_created, failed_rows = create_recipe_by_list(df)
        
        return success_response({
            "message": f"{new_created} production recipes created successfully",
            "failed_rows": failed_rows
        })
    except Exception as e:
        # Capture les erreurs globales non gérées
        return error_response(str(e), 500)

@production_recipe_bp.route('/production_recipes', methods=['GET'])
def get_production_recipes():
    try:
        raw_params = request.args.to_dict()
        
        # On s'assure que parse_filter_params existe, sinon on utilise raw_params
        # filter_params = parse_filter_params(raw_params) 
        filter_params = raw_params # Simplification si pas de fonction de parsing complexe

        # CORRECTION 1 : Passage correct de l'argument 'filters'
        result = read_recipe(filters=filter_params)

        # CORRECTION 2 & 3 : Gestion du retour unique vs liste pour Marshmallow
        schema = ProductionRecipeSchema(many=True) # On prépare un schema pour liste
        
        if result is None:
            recipes_data = []
        elif isinstance(result, list):
            # C'est déjà une liste
            recipes_data = schema.dump(result)
        else:
            # C'est un objet unique (cas du filtre 'code'), on le met dans une liste
            # pour garder la cohérence de la réponse JSON "recettes": [...]
            single_schema = ProductionRecipeSchema(many=False)
            recipes_data = [single_schema.dump(result)]

        return success_response(
            data={"recettes": recipes_data},
            message="Recettes filtrées récupérées avec succès",
            status_code=200
        )
    except Exception as e:
        return error_response(f"Erreur lors du filtrage des recettes : {str(e)}", 500)
    