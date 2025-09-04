# BACKEND\app\common\base\base_model.py

import uuid
from datetime import datetime
from app.core.extensions import db 

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"
    
    def save(self, commit=True):
        try:
            db.session.add(self)
            if commit:
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            # Ici tu peux logger l’erreur ou la re-raise
            raise e

    def delete(self, commit=True):
        try:
            db.session.delete(self)
            if commit:
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e



