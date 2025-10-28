# BACKEND/app/modules/articles/schemas/marques/marque_schema.py

from marshmallow import pre_load
from app.common.base.base_schema import BaseSchema
from app.core.extensions import db
from app.modules.articles.models.marques import Marque  # chemin corrigé

class MarqueSchema(BaseSchema):
    """
    Schéma spécifique pour le modèle Marque.
    Convertit le champ 'nom' en majuscules avant chargement.
    """
    class Meta:
        model = Marque
        load_instance = True
        include_fk = True
        sqla_session = db.session

    @pre_load
    def uppercase_nom(self, data, **kwargs):
        if "nom" in data and isinstance(data["nom"], str):
            data["nom"] = data["nom"].upper().strip()
        return data