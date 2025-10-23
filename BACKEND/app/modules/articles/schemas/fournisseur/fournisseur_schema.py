# BACKEND\app\modules\articles\schemas\fournisseur\fournisseur_schema.py

from app.common.base.base_schema import BaseSchema
from app.core.extensions import db

from app.modules.articles.models import Fournisseur

class FournisseurSchema(BaseSchema):
    """
    Schéma spécifique pour le modèle Marque.
    On pourra ajouter ici des champs supplémentaires ou des nested fields.
    """
    class Meta:
        model = Fournisseur
        load_instance = True
        include_fk = True
        sqla_session = db.session  # Correctement placé au niveau de Meta