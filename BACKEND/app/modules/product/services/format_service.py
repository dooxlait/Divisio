# BACKEND/app/modules/product/services/format_service.py

from app.core.extensions import db
from app.modules.product.models.format import Format

class FormatService:
    """Service pur pour gérer les formats des produits"""

    def get_all(self):
        """Retourne tous les formats"""
        return Format.query.all()

    def get_by_id(self, format_id):
        """Retourne un format par son ID"""
        return Format.query.get(format_id)

    def create(self, data):
        """
        Crée un format de produit.
        data doit être validé par le schema (FormatCreateSchema)
        """
        format_obj = Format(**data)
        db.session.add(format_obj)
        db.session.commit()
        return format_obj

    def update(self, format_id, data):
        """
        Met à jour un format existant.
        data doit être validé par le schema (FormatUpdateSchema)
        """
        format_obj = self.get_by_id(format_id)
        if not format_obj:
            return None
        for key, value in data.items():
            setattr(format_obj, key, value)
        db.session.commit()
        return format_obj

    def delete(self, format_id):
        """Supprime un format"""
        format_obj = self.get_by_id(format_id)
        if not format_obj:
            return False
        db.session.delete(format_obj)
        db.session.commit()
        return True
