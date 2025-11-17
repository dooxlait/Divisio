# BACKEND\app\modules\production\schemas\production_order\production_order_schema.py

from app.modules.production.models.production_order import ProductionOrder
from app.common.base.base_schema import BaseSchema
from app.core.extensions import db

class ProductionOrderSchema(BaseSchema):
    """
    Schéma spécifique pour le modèle ProductionOrder.
    On pourra ajouter ici des champs supplémentaires ou des nested fields.
    """
    class Meta:
        model = ProductionOrder
        load_instance = True
        include_fk = True
        sqla_session = db.session  # Correctement placé au niveau de Meta