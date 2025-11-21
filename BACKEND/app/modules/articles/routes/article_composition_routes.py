from flask import Blueprint, request
from app.common.helper import fusionner_onglets_excel
from app.common.response.response import success_response, error_response
from app.modules.articles.services.article_composition import rajoute_dlc_dgr_aux_articles, rajouter_gamme_aux_articles, rajouter_infos_etiquettes_colis_aux_articles
article_composition_bp = Blueprint('article_composition_bp', __name__, url_prefix='/article-compositions')

@article_composition_bp.route("/import-dlc-dgr", methods=["POST"])
def import_dlc_dgr():
    file = request.files.get("file")
    
    if not file:
        return error_response("Aucun fichier fourni", 400)
    
    if not file.filename.endswith('.xlsx'):
        return error_response("Le fichier fourni n'a pas la bonne extension (*.xlsx requis)", 400)
    
    # création du DataFrame à partir du fichier Excel
    df = fusionner_onglets_excel(file)
    
    # mise à jour des articles avec DLC/DGR
    count_caracteristiques = rajoute_dlc_dgr_aux_articles(df)
    count_gamme = rajouter_gamme_aux_articles(df)
    etiquettes_colis = rajouter_infos_etiquettes_colis_aux_articles(df)
    
    return success_response(
        data={
            "updated": count_caracteristiques,
            "updated_gamme": count_gamme,
            "etiquettes_colis": etiquettes_colis
        },
        message="DLC/DGR importées avec succès",
        status_code=200
    )
    