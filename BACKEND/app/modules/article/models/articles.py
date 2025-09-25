from app.common.base.base_model import BaseModel
from app.core.extensions import db

class Article(BaseModel): 
    __tablename__ = "articles"
    nom_article = db.Column(db.String(36), db.ForeignKey("divisions.id"), nullable=False)
    code_externe = db.Column(db.String(36), db.ForeignKey("divisions.id"), nullable=False)
