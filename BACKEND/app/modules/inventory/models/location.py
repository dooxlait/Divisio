# BACKEND\app\modules\inventory\models\location.py

from sqlalchemy import UniqueConstraint, ForeignKey
from app.common.base.base_model import BaseModel
from app.core.extensions import db


class Location(BaseModel):
    __tablename__ = "locations"
    __table_args__ = (
        UniqueConstraint("site_id", "code", name="uq_location_site_code"),
    )

    site_id = db.Column(db.String(36), ForeignKey("sites.id"), nullable=False)
    code = db.Column(db.String(50), nullable=False)   # Identifiant local ex: "A1-R2"
    description = db.Column(db.String(255), nullable=True)

    # Relations
    site = db.relationship("Site", backref=db.backref("locations", lazy=True))

    def __repr__(self):
        return f"<Location {self.code} (site={self.site_id})>"
