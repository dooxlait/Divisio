# BACKEND\app\modules\articles\schemas\palettisation\palletisation_read_schema.py

from app.common.base.base_schema import BaseSchema
from app.core.extensions import db

from app.modules.articles.models import Palettisation

class PalettisationReadSchema(BaseSchema):
    """
    Schéma spécifique pour le modèle Unite.
    On pourra ajouter ici des champs supplémentaires ou des nested fields.
    """
    class Meta:
        model = Palettisation
        load_instance = True
        include_fk = True
        sqla_session = db.session  # Correctement placé au niveau de Meta