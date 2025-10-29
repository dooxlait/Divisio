from app.common.base.base_schema import BaseSchema
from app.core.extensions import ma
from app.modules.articles.models import ArticleComposition


class ArticleCompositionSchema(BaseSchema):
    """
    Schéma pour ArticleComposition
    Inclut le composant (Article) imbriqué.
    """

    # UUID pour clés étrangères
    article_id = ma.String()
    component_id = ma.String()

    # Relation vers l'article composant
    component = ma.Nested("ArticleReadSchema", only=["code", "designation"], dump_only=True)

    class Meta:
        model = ArticleComposition
        load_instance = True
        include_fk = True
        sqla_session = None  # utilisera session globale de BaseSchema
