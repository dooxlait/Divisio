from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy import UniqueConstraint, ForeignKey

class Unite(BaseModel):
    __tablename__ = "unites"

    code = db.Column(db.String(50), nullable=False, unique=True)  # KG, L, PCE…
    designation = db.Column(db.String(50), nullable=False)        # Kilogramme, Litre, Pièce…
    type_unite = db.Column(db.String(255), nullable=False)        # Masse, Volume, Quantité…
    facteur_conversion = db.Column(db.Float, nullable=False, default=1.0)  # Conversion vers unité de référence
