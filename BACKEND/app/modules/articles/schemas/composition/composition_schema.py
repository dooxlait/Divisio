    
# app/modules/articles/schemas/composition.py

from app.common.base.base_schema import BaseSchema
from app.core.extensions import ma
from app.modules.articles.models import ArticleComposition
from marshmallow import fields

class ArticleCompositionSchema(BaseSchema):
    """
    Schéma pour ArticleComposition.
    Fait le lien entre un Article Parent et un Article Enfant (Composant).
    """

    # =================================================================
    # 1. CLÉS ÉTRANGÈRES (Mise à jour des noms)
    # =================================================================
    # Remplace article_id
    article_parent_id = fields.String(dump_only=True)
    
    # Remplace component_id
    article_enfant_id = fields.String(dump_only=True)
    
    unite_id = fields.String(dump_only=True)
    
    # =================================================================
    # 2. DONNÉES PROPRES
    # =================================================================
    quantite = fields.Decimal(as_string=False, dump_default=0)

    # =================================================================
    # 3. RELATIONS IMBRIQUÉES
    # =================================================================
    
    # Remplace 'component'. 
    # C'est l'article "Enfant" (le pot, l'opercule, le vrac) qu'on veut afficher.
    # On utilise une chaîne "ArticleReadSchema" pour éviter les imports circulaires.
    article_enfant = ma.Nested(
        "ArticleReadSchema", 
        only=["id", "code", "designation", "type_article", "unite_code"], 
        dump_only=True
    )

    # Optionnel : Afficher le code de l'unité de consommation (ex: "pce", "kg")
    unite = ma.Nested("UniteSchema", only=["code"], dump_only=True)

    class Meta:
        model = ArticleComposition
        load_instance = True
        include_fk = True
        sqla_session = None

  