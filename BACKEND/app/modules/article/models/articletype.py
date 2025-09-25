from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy import UniqueConstraint, ForeignKey

class ArticleType(BaseModel):
    __tablename__ = "articles_type"
    __table_args__ = (
        UniqueConstraint(),
    )
    
    code = db.Column(db.String(50), nullable=False, unique=True)
    designation = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
