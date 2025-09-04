# BACKEND\app\modules\inventory\models\inventory_balance.py

from sqlalchemy import UniqueConstraint, ForeignKey
from app.common.base.base_model import BaseModel
from app.core.extensions import db


class InventoryBalance(BaseModel):
    __tablename__ = "inventory_balances"
    __table_args__ = (
        UniqueConstraint("article_id", "location_id", name="uq_article_location"),
    )

    article_id = db.Column(db.String(36), ForeignKey("articles.id"), nullable=False)
    location_id = db.Column(db.String(36), ForeignKey("locations.id"), nullable=False)
    quantity = db.Column(db.Float, nullable=False, default=0.0)

    # Relations
    article = db.relationship("Article", backref=db.backref("balances", lazy=True))
    location = db.relationship("Location", backref=db.backref("balances", lazy=True))

    def __repr__(self):
        return f"<InventoryBalance article={self.article_id}, location={self.location_id}, qty={self.quantity}>"
