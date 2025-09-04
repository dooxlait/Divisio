# D:\Dev\_apps\DIVISIO\BACKEND\app\modules\inventory\models\article.py

from sqlalchemy import UniqueConstraint
from app.common.base.base_model import BaseModel
from app.core.extensions import db


class Article(BaseModel):
    __tablename__ = "articles"
    __table_args__ = (
        UniqueConstraint("sku", name="uq_article_sku"),
    )

    name = db.Column(db.String(100), nullable=False)   # Nom lisible
    sku = db.Column(db.String(50), nullable=False)     # Code article interne unique
    category = db.Column(db.String(50), nullable=True) # ex: "matière", "fini", "emballage", "pièce détachée"
    unit = db.Column(db.String(20), nullable=False, default="pcs")  # Unité de mesure

    def __repr__(self):
        return f"<Article {self.name} ({self.sku})>"
