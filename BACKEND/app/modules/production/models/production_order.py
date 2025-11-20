# app/modules/production/models/production_order.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db
from datetime import date


class ProductionOrder(BaseModel):
    __tablename__ = "production_orders"

    # =================================================================== #
    #                      COLONNES OBLIGATOIRES                          #
    # =================================================================== #
    reference = db.Column(db.String(50), unique=True, nullable=True) # Référence personnalisée de l'ordre de production
    article_id = db.Column(db.String(36), db.ForeignKey("articles.id"), nullable=False)
    unite_article_id = db.Column(db.String(36), db.ForeignKey("unites.id"), nullable=False)

    quantity_planned = db.Column(db.Numeric(12, 4), nullable=False)
    quantity_produced = db.Column(db.Numeric(12, 4), default=0)
    quantity_depreciated = db.Column(db.Numeric(12, 4), default=0)
    
    product_DLC = db.Column(db.Date, nullable=True)
    product_DGR = db.Column(db.Date, nullable=True)
    
    fabrication_start_date_planned = db.Column(db.Date, nullable=False)
    fabrication_start_date_real = db.Column(db.Date, nullable=True)
    fabrication_end_date_real = db.Column(db.Date, nullable=True)
    
    status = db.Column(db.String(20), default="planned")  # planned, in_progress, finished, cancelled
    priority = db.Column(db.String(10), default="normal")
    notes = db.Column(db.Text, nullable=True)
    ligne_id = db.Column(db.String(36), db.ForeignKey("divisions.id"),nullable=True)
    # ===================================================================
    #                           RELATIONSHIPS 
    # ===================================================================
    article = db.relationship(
        "Article",
        back_populates="production_orders"
    )

    unite = db.relationship(
        "Unite",
        back_populates="production_orders"
    )
    
    ligne = db.relationship("Division",
        backref=db.backref("production_orders", lazy=True),
        foreign_keys=[ligne_id] 
    )

    # Optionnel : si tu veux aussi les consommations, mouvements, etc.
    # consumptions = db.relationship("Consumption", back_populates="production_order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<OF {self.reference or self.id} - {self.article.code if self.article else ''}>"