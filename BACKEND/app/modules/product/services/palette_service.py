# BACKEND/app/modules/product/services/palette_service.py

from app.core.extensions import db
from app.modules.product.models.palette import Palette

class PaletteService:
    """Service pur pour gérer les palettes"""

    def get_all(self):
        """Retourne toutes les palettes"""
        return Palette.query.all()

    def get_by_id(self, palette_id):
        """Retourne une palette par son ID"""
        return Palette.query.get(palette_id)

    def create(self, data):
        """Créer une palette, data doit être validé par le schema"""
        palette = Palette(**data)
        db.session.add(palette)
        db.session.commit()
        return palette

    def update(self, palette_id, data):
        """Mettre à jour une palette existante, data doit être validé par le schema"""
        palette = self.get_by_id(palette_id)
        if not palette:
            return None
        for key, value in data.items():
            setattr(palette, key, value)
        db.session.commit()
        return palette

    def delete(self, palette_id):
        """Supprimer une palette"""
        palette = self.get_by_id(palette_id)
        if not palette:
            return False
        db.session.delete(palette)
        db.session.commit()
        return True
