from app.core.extensions import db
from app.common.base.base_model import BaseModel

from app.core.extensions import db
from app.common.base.base_model import BaseModel

class ArticleComposition(BaseModel):
    __tablename__ = "article_compositions"

    # ===============================================================
    # COLONNES (DOIVENT CORRESPONDRE EXACTEMENT A 'ARTICLE')
    # ===============================================================
    
    # C'est cette colonne que SQLAlchemy ne trouvait pas
    article_parent_id = db.Column(db.String(36), db.ForeignKey("articles.id"), nullable=False)
    
    # Et celle-ci pour le composant
    article_enfant_id = db.Column(db.String(36), db.ForeignKey("articles.id"), nullable=False)
    
    quantite = db.Column(db.Numeric(12, 4), nullable=False)
    unite_id = db.Column(db.String(36), db.ForeignKey("unites.id"), nullable=True)

    # ===============================================================
    # RELATIONSHIPS
    # ===============================================================
    
    # Lien vers le Produit Fini (Parent)
    article_parent = db.relationship(
        "Article",
        foreign_keys=[article_parent_id], # On précise quelle colonne utiliser
        back_populates="composition_enfants"
    )
    
    # Lien vers le Composant (Enfant)
    article_enfant = db.relationship(
        "Article",
        foreign_keys=[article_enfant_id], # On précise quelle colonne utiliser
        back_populates="composition_parents"
    )
    
    unite = db.relationship("Unite")