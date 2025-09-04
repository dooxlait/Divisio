from app.common.base.base_model import BaseModel
from app.core.extensions import db

class Site(BaseModel):
    __tablename__ = "sites"
    
    name = db.Column(db.String(50), nullable=False, unique=True)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(55), nullable=False)

    address = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<Site {self.name} - {self.city}, {self.country}>"