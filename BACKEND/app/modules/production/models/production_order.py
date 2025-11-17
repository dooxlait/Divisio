# BACKEND\app\modules\production\models\production_order.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy import ForeignKey

class ProductionOrder(BaseModel):
    __tablename__ = "production_orders"

    reference = db.Column(db.String(50), nullable=False, unique=True)  # N° d’OF
    quantity_planned = db.Column(db.Integer, nullable=False)
    quantity_produced = db.Column(db.Integer, nullable=True)

    status = db.Column(db.String(20), nullable=False, default="planned")  
    # planned / in_progress / completed / cancelled

    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)

    # --- Lien vers Article ---
    article_id = db.Column(db.String(36), db.ForeignKey("articles.id"), nullable=False)
    article = db.relationship("Article", back_populates="production_orders")

    def __repr__(self):
        return f"<ProductionOrder {self.reference} - {self.product_name} ({self.status})>"

