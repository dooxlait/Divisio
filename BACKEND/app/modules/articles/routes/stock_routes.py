# BACKEND\app\modules\articles\routes\stock_routes.py

from flask import Blueprint, request, jsonify
from app.common.response.response import success_response, error_response
from app.modules.articles.services.stock_service import *
from app.modules.articles.schemas import StockSchema
from app.common.helper.excel_helper import *

stock_bp = Blueprint('stock', __name__, url_prefix="/stocks")

@stock_bp.route("/listearticlestock", methods=["GET"])
def create_liste_article_stock():
    """ Route pour créer la liste des articles en stock. """
    
    try:
        liste_stock = creer_liste_article_stock()
        schema = StockSchema(many=True)
        stock_data = schema.dump(liste_stock)
        return success_response(
            data={"liste_stock": stock_data},
            message="Liste des articles en stock créée avec succès",
            status_code=200
        )
    except Exception as e:
        return error_response(
            message=f"Erreur lors de la création de la liste des articles en stock: {str(e)}",
            status_code=500
        )

@stock_bp.route("/", methods=["POST"])
def create_stock():
    """ Route pour créer une nouvelle entrée de stock. """
    
    data = request.get_json()
    if not data:
        return error_response(
            message="Données invalides fournies",
            status_code=400
        )
    try:
        new_stock = ecrire_en_stock(**data)
        schema = StockSchema()
        stock_data = schema.dump(new_stock)
        return success_response(
            data={"stock": stock_data},
            message="Stock créé avec succès",
            status_code=201
        )
    except Exception as e:
        return error_response(
            message=f"Erreur lors de la création du stock: {str(e)}",
            status_code=500
        )
        
@stock_bp.route('/stockbyexcel', methods=['POST'])
def ecrire_stock_par_excel():
    """ Route pour écrire des entrées de stock à partir d'un fichier Excel. """
    
    if 'file' not in request.files:
        return error_response(
            message="Aucun fichier fourni",
            status_code=400
        )
    file = request.files['file']
    if file.filename == '':
        return error_response(
            message="Nom de fichier invalide",
            status_code=400
        )
    try:
        df_stock = lire_excel(file)
        stocks = ecrire_stock_par_excel(df_stock)
        schema = StockSchema(many=True)
        stocks_data = schema.dump(stocks)
        return success_response(
            data={"stocks": stocks_data},
            message="Stocks écrits avec succès à partir du fichier Excel",
            status_code=201
        )
    except Exception as e:
        return error_response(
            message=f"Erreur lors de l'écriture des stocks à partir du fichier Excel: {str(e)}",
            status_code=500
        )
        
@stock_bp.route("/", methods=["GET"])
def get_all_stocks():
    """ Route pour récupérer toutes les entrées de stock. """
    
    try:
        stocks = obtenir_tout_le_stock()
        schema = StockSchema(many=True)
        stocks_data = schema.dump(stocks)
        return success_response(
            data={"stocks": stocks_data},
            message="Liste des stocks récupérée avec succès",
            status_code=200
        )
    except Exception as e:
        return error_response(
            message=f"Erreur lors de la récupération des stocks: {str(e)}",
            status_code=500
        )   
        
@stock_bp.route("/<int:stock_id>", methods=["GET"])
def get_stock_by_id(stock_id):
    """ Route pour récupérer une entrée de stock par ID. """
    
    try:
        stock = obtenir_stock_par_id(stock_id)
        if not stock:
            return error_response(
                message="Stock non trouvé",
                status_code=404
            )
        schema = StockSchema()
        stock_data = schema.dump(stock)
        return success_response(
            data={"stock": stock_data},
            message="Stock récupéré avec succès",
            status_code=200
        )
    except Exception as e:
        return error_response(
            message=f"Erreur lors de la récupération du stock: {str(e)}",
            status_code=500
        )
        
@stock_bp.route("/<int:stock_id>", methods=["PUT"])
def update_stock(stock_id):
    """ Route pour mettre à jour une entrée de stock existante. """
    
    data = request.get_json()
    if not data:
        return error_response(
            message="Données invalides fournies",
            status_code=400
        )
    try:
        updated_stock = mettre_a_jour_stock(stock_id, **data)
        if not updated_stock:
            return error_response(
                message="Stock non trouvé",
                status_code=404
            )
        schema = StockSchema()
        stock_data = schema.dump(updated_stock)
        return success_response(
            data={"stock": stock_data},
            message="Stock mis à jour avec succès",
            status_code=200
        )
    except Exception as e:
        return error_response(
            message=f"Erreur lors de la mise à jour du stock: {str(e)}",
            status_code=500
        )