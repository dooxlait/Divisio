from app.common.base.base_model import BaseModel
from app.core.extensions import db

class Category(BaseModel):
    __tablename__ = 'categories'

    code = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # relationships
    articles = db.relationship("Article", back_populates="category")