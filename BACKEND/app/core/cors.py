from flask_cors import CORS

def init_cors(app):
    """
    Initialise la configuration CORS de manière centralisée.
    """
    CORS(
        app,
        resources={
            r"/api/*": {   # seulement les routes API
                "origins": ["http://localhost:3000", "http://192.168.56.1:3000"],  # whitelist
                "methods": ["GET", "POST", "PUT", "PATCH", "DELETE"],
                "allow_headers": ["Content-Type", "Authorization"],
                "supports_credentials": True
            }
        }
    )
