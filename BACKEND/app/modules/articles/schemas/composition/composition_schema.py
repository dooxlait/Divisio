from app.common.base.base_schema import BaseSchema
from app.modules.articles.models.composition import ArticleComposition
from app.core.extensions import db

class ArticleCompositionSchema(BaseSchema):
    class Meta:
        model = ArticleComposition
        load_instance = True
        include_fk = True
        sqla_session = db.session  # Correctement placé au niveau de Meta
