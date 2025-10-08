# BACKEND\app\modules\article\models\articlecomposition.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class ArticleComposition(BaseModel):
    __tablename__ = "articles_compositions"

    parent_article_id = db.Column(db.String(36), ForeignKey("articles.id"), nullable=False)
    composant_article_id = db.Column(db.String(36), ForeignKey("articles.id"), nullable=False)
    quantite = db.Column(db.Float, nullable=False, default=1.0)

    # Relations vers Article
    article_parent = relationship(
        "Article",
        foreign_keys=[parent_article_id],
        back_populates="composants"
    )

    article_composant = relationship(
        "Article",
        foreign_keys=[composant_article_id],
        back_populates="inclus_dans"
    )

    __table_args__ = (
        db.UniqueConstraint("parent_article_id", "composant_article_id", name="uq_article_compo"),
    )