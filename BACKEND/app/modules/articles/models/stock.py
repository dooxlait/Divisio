# BACKEND\app\modules\articles\models\stock.py

from sqlalchemy import Integer
from app.core.extensions import db
from app.common.base.base_model import BaseModel

class Stock(BaseModel):
    __tablename__ = "stocks"

    id_article = db.Column(
        db.String(36),
        db.ForeignKey("articles.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False
    )
    id_unite = db.Column(
        db.String(36),
        db.ForeignKey("unites.id", ondelete="SET NULL", onupdate="CASCADE"),
        nullable=True
    )

    quantity = db.Column(Integer, nullable=False, default=0)
    location = db.Column(db.String(255), nullable=True)
    dlc = db.Column(db.Date, nullable=True)
    numero_lot = db.Column(db.String(100), nullable=True)
    is_bloque = db.Column(db.Boolean, nullable=False, default=False)

    article = db.relationship("Article", back_populates="stocks")
    unite = db.relationship("Unite", back_populates="stocks")
    mouvements = db.relationship("MouvementStock", back_populates="stock", cascade="all, delete-orphan")

    __table_args__ = (
        db.Index('idx_stock_article', 'id_article'),
        db.Index('idx_stock_lot', 'numero_lot'),
    )
