# app/modules/production/models/production_order.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db
from datetime import date


class ProductionOrder(BaseModel):
    __tablename__ = "production_orders"

    # =================================================================== #
    #                      COLONNES OBLIGATOIRES                          #
    # =================================================================== #
    reference = db.Column(db.String(50), unique=True, nullable=True)
    
    # QUOI : L'article à produire
    article_id = db.Column(db.String(36), db.ForeignKey("articles.id"), nullable=False)
    unite_article_id = db.Column(db.String(36), db.ForeignKey("unites.id"), nullable=False)

    # COMMENT : La recette utilisée (Si c'est un OF de Process type VRAC/BASE)
    # Nullable car un OF de conditionnement n'utilise pas forcément une "ProductionRecipe" mais une "Composition"
    recipe_id = db.Column(db.String(36), db.ForeignKey("production_recipes.id"), nullable=True)

    # TRAÇABILITÉ : Le numéro de lot créé par cet OF (Vital pour Agro)
    batch_number = db.Column(db.String(50), nullable=True, index=True)

    # =================================================================== #
    #                            QUANTITÉS                                #
    # =================================================================== #
    quantity_planned = db.Column(db.Numeric(12, 4), nullable=False)
    quantity_produced = db.Column(db.Numeric(12, 4), default=0)
    
    # Renommé pour plus de clarté métier (Rebuts/Pertes)
    quantity_rejected = db.Column(db.Numeric(12, 4), default=0)
    
    # =================================================================== #
    #                        DATES & PLANNING                             #
    # =================================================================== #
    # Gestion DLC/DGR
    product_DLC = db.Column(db.Date, nullable=True) # Date limite du produit sorti
    product_DGR = db.Column(db.Date, nullable=True) # Date garantie client visée
    
    # Planning (Date suffit souvent)
    fabrication_start_date_planned = db.Column(db.Date, nullable=False)
    
    # Réel (DateTime est mieux pour calculer la productivité horaire)
    fabrication_start_date_real = db.Column(db.DateTime, nullable=True)
    fabrication_end_date_real = db.Column(db.DateTime, nullable=True)
    
    # =================================================================== #
    #                        STATUT & CONTEXTE                            #
    # =================================================================== #
    status = db.Column(db.String(20), default="planned") # planned, in_progress, finished, cancelled
    priority = db.Column(db.String(10), default="normal")
    notes = db.Column(db.Text, nullable=True)
    
    # Ligne de production (Atelier)
    ligne_id = db.Column(db.String(36), db.ForeignKey("divisions.id"), nullable=True)

    # ===================================================================
    #                           RELATIONSHIPS 
    # ===================================================================
    article = db.relationship(
        "Article",
        back_populates="production_orders"
    )
    
    # Lien vers la recette (Process)
    recipe = db.relationship(
        "ProductionRecipe",
        back_populates="production_orders"
    )

    unite = db.relationship(
        "Unite",
        back_populates="production_orders" # Assurez-vous que Unite a bien cette relation
    )
    
    ligne = db.relationship(
        "Division",
        backref=db.backref("production_orders", lazy=True),
        foreign_keys=[ligne_id] 
    )

    def __repr__(self):
        return f"<OF {self.reference or self.id} - {self.status}>"