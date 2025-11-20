# BACKEND\app\modules\production\schemas\production_order\production_order_create_schema.py

from app.common.base.base_schema import BaseSchema
from app.core.extensions import db
from marshmallow import post_load, ValidationError, validates, fields
from datetime import datetime
from app.modules.production.models.production_order import ProductionOrder

# --- Génération de la référence annuelle ---
def generate_of_reference(article_code: str) -> str:
    today = datetime.now()
    year_str = today.strftime("%Y")  # Année en 4 chiffres

    start_of_year = datetime(today.year, 1, 1)

    count_year = (
        ProductionOrder.query
        .filter(ProductionOrder.article.has(code=article_code))
        .filter(ProductionOrder.created_at >= start_of_year)
        .count()
    ) + 1

    return f"OF-{year_str}-{article_code}-{str(count_year).zfill(3)}"

# --- Schéma Marshmallow ---
class ProductionOrderCreateSchema(BaseSchema):
    """
    Schéma pour la création d'un ordre de production.
    Contient uniquement les champs nécessaires à la création.
    """
    status = fields.String(missing="planned")
    
    class Meta:
        model = ProductionOrder
        load_instance = False
        include_fk = True
        sqla_session = db.session

    @validates("status")
    def validate_status(self, value):
        allowed = {"planned", "in_progress", "completed", "cancelled"}
        if value not in allowed:
            raise ValidationError(
                f"Le status doit être l'un de {', '.join(allowed)}"
            )


    @post_load
    def make_production_order(self, data, **kwargs):
        from app.modules.articles.models.articles import Article  # import local
        article = Article.query.get(data['article_id'])
        if not article:
            raise ValidationError("Article non trouvé")
        
        data['reference'] = generate_of_reference(article.code)
        return data

