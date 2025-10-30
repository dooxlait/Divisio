from app.common.base.base_schema import BaseSchema
from app.core.extensions import db

from app.modules.articles.models import CaracteristiqueArticle

class CaracteristiqueArticleSchema(BaseSchema):
    """
    Schéma spécifique pour le modèle Category.
    On pourra ajouter ici des champs supplémentaires ou des nested fields.
    """
    class Meta:
        model = CaracteristiqueArticle
        load_instance = True
        include_fk = True
        sqla_session = db.session  # Correctement placé au niveau de Meta