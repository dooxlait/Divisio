# BACKEND\app\modules\inventory\models\inventory_transaction.py

from sqlalchemy import ForeignKey
from app.common.base.base_model import BaseModel
from app.core.extensions import db


class InventoryTransaction(BaseModel):
    __tablename__ = "inventory_transactions"

    article_id = db.Column(db.String(36), ForeignKey("articles.id"), nullable=False)
    from_location_id = db.Column(db.String(36), ForeignKey("locations.id"), nullable=True)
    to_location_id = db.Column(db.String(36), ForeignKey("locations.id"), nullable=True)

    quantity = db.Column(db.Float, nullable=False)   # quantité transférée (+ ou -)
    transaction_type = db.Column(db.String(20), nullable=False)  # "in", "out", "transfer", "adjustment"

    # Relations
    article = db.relationship("Article", backref=db.backref("transactions", lazy=True))
    from_location = db.relationship("Location", foreign_keys=[from_location_id])
    to_location = db.relationship("Location", foreign_keys=[to_location_id])

    def __repr__(self):
        return f"<InventoryTransaction article={self.article_id}, qty={self.quantity}, type={self.transaction_type}>"
