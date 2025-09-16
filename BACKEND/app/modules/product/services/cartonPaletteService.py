# BACKEND/app/modules/product/services/carton_palette_service.py

from app.core.extensions import db
from app.modules.product.models.carton_palette import CartonPalette

class CartonPaletteService:
    """Service pur pour gérer les associations carton ↔ palette"""

    def get_all(self):
        return CartonPalette.query.all()

    def get_by_id(self, cp_id):
        return CartonPalette.query.get(cp_id)

    def create(self, data):
        cp = CartonPalette(**data)
        db.session.add(cp)
        db.session.commit()
        return cp

    def update(self, cp_id, data):
        cp = self.get_by_id(cp_id)
        if not cp:
            return None
        for key, value in data.items():
            setattr(cp, key, value)
        db.session.commit()
        return cp

    def delete(self, cp_id):
        cp = self.get_by_id(cp_id)
        if not cp:
            return False
        db.session.delete(cp)
        db.session.commit()
        return True
