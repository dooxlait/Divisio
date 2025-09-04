# BACKEND/app/modules/factory/schemas/factory/factory_schema.py

from app.common.base.base_schema import BaseSchema
from app.modules.factory.models.site import Site

class SiteSchema(BaseSchema):
    """
    Schéma spécifique pour le modèle Factory.
    On pourra ajouter ici des champs supplémentaires ou des nested fields.
    """
    class Meta:
        model = Site
        load_instance = True
