from .models.carton_palette import CartonPalette
from .models.carton import Carton
from .models.coiffe import Coiffe
from .models.format import Format
from .models.opercule import Opercule
from .models.origine import Origine
from .models.palette import Palette
from .models.pot import Pot
from .models.produit_carton import ProduitCarton
from.models.produit_emballage import ProduitEmballage
from .models.produit_fini import ProduitFini
from .models.type_produit import TypeProduit
from .models.variante import Variante


# Import des blueprints
from app.modules.product.routes.carton_routes import carton_bp
from app.modules.product.routes.carton_palette_routes import carton_palette_bp
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

def register_products_routes(app, url_prefix="/products"):
    """
    Enregistre tous les blueprints du module product dans l'application Flask.
    """
    app.register_blueprint(carton_bp)
    app.register_blueprint(carton_palette_bp)
    app.register_blueprint(coiffe_bp)
    app.register_blueprint(format_bp)
    app.register_blueprint(opercule_bp)
    app.register_blueprint(origine_bp)
    app.register_blueprint(palette_bp)
    app.register_blueprint(pot_bp)
    app.register_blueprint(produit_emballage_bp)
    app.register_blueprint(produit_fini_bp)
    app.register_blueprint(produit_carton_bp)
    app.register_blueprint(type_produit_bp)
    app.register_blueprint(variante_bp)