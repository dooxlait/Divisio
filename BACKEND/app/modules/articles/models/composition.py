from app.core.extensions import db
from app.common.base.base_model import BaseModel

from app.core.extensions import db
from app.common.base.base_model import BaseModel

class ArticleComposition(BaseModel):
    __tablename__ = "article_compositions"

    article_id = db.Column(db.Integer, db.ForeignKey("articles.id"), nullable=False)
    component_id = db.Column(db.Integer, db.ForeignKey("articles.id"), nullable=False)
    quantity = db.Column(db.Float, nullable=False)

    # Relations
    article = db.relationship(
        "Article",
        foreign_keys=[article_id],
        back_populates="compositions"
    )
    component = db.relationship(
        "Article",
        foreign_keys=[component_id]
    )