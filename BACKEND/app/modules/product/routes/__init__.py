# BACKEND\app\modules\product\routes\__init__.py


# Import des blueprints
from app.modules.product.routes.carton_routes import carton_bp
from app.modules.product.routes.carton_palette_routes import produit_carton_bp as carton_palette_bp
from app.modules.product.routes.coiffe_routes import coiffe_bp
from app.modules.product.routes.format_routes import format_bp
from app.modules.product.routes.opercule_routes import opercule_bp
from app.modules.product.routes.origine_routes import origine_bp
from app.modules.product.routes.palette_routes import palette_bp
from app.modules.product.routes.pot_routes import pot_bp
from app.modules.product.routes.produit_emballage_routes import produit_emballage_bp
from app.modules.product.routes.produit_fini_routes import produit_fini_bp
from app.modules.product.routes.produit_carton_routes import produit_carton_bp
from app.modules.product.routes.type_produit_routes import type_produit_bp
from app.modules.product.routes.variante_routes import variante_bp