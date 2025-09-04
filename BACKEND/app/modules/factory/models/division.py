# BACKEND\app\modules\factory\models\division.py

from sqlalchemy import UniqueConstraint, ForeignKey

from app.common.base.base_model import BaseModel
from app.core.extensions import db

class Division(BaseModel):
    __tablename__ = 'divisions'
    __table_args__ = (
        UniqueConstraint('site_id', 'type', 'name', name='uq_division_site'),
    )

    site_id = db.Column(db.String(36), db.ForeignKey("sites.id"), nullable=False)
    type = db.Column(db.String(50), nullable=False)   # ex: "service", "atelier", "ligne"
    name = db.Column(db.String(50), nullable=False)   # ex: "Production", "R&D", "Atelier animal"
    parent_id = db.Column(db.String(36), ForeignKey("divisions.id"), nullable=True)  

    # --- Relations ---
    parent = db.relationship(
        "Division",
        remote_side="Division.id",  # auto-référence correcte
        backref=db.backref("subdivisions", lazy=True)
    )

    # 👉 si tu veux rattacher des directeurs/chefs : fais une table de liaison séparée (DivisionDirector)
    # Ici je supprime le db.relationship("Employee") car ça ne marche pas sans clé étrangère

    def __repr__(self):
        return f"<Division id={self.id}, name={self.name}, type={self.type}>"