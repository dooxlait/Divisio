# BACKEND\app\modules\articles\schemas\stock\stock_schema.py

from app.common.base.base_schema import BaseSchema
from app.core.extensions import db

from app.modules.articles.models import Stock

class StockSchema(BaseSchema):
    """
    Schéma spécifique pour le modèle Stock.
    On pourra ajouter ici des champs supplémentaires ou des nested fields.
    """
    class Meta:
        model = Stock
        load_instance = True
        include_fk = True
        sqla_session = db.session  # Correctement placé au niveau de Meta