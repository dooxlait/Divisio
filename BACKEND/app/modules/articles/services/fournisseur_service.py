from app.modules.articles.models import Fournisseur


def get_all_fournisseurs():
    fournisseurs = Fournisseur.query.all()
    return fournisseurs

