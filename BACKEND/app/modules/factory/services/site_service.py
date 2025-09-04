# BACKEND\app\modules\factory\services\site_service.py

from app.core.extensions import db
from app.modules.factory.models.site import Site

def get_all_sites():
    return Site.query.all()

def create_site_service(site):
    try:
        db.session.add(site)
        db.session.commit()
        return site
    except Exception as e:
        db.session.rollback()
        print(f"[ERREUR] Échec création site: {e}")
        return None
