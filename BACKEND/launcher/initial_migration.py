# BACKEND/launcher/initial_migration.py

from app import create_app
from .launcher_service import insert_if_empty

# ===================================================================
# CRÉATION DE L'APP + CONTEXTE AVANT TOUT IMPORT DE MODÈLES/SCHEMAS
# ===================================================================
app = create_app()
print("[COLD START] - Peuplement de la base de données")

with app.app_context():
    # ===============================================================
    # TOUS LES IMPORTS DE MODÈLES ET SCHÉMAS DOIVENT ÊTRE ICI !
    # ===============================================================
    from app.modules.factory.models.site import Site
    from app.modules.factory.schemas.site.SiteCreateSchema import SiteCreateSchema
    from app.modules.factory.models.division import Division
    from app.modules.factory.schemas.division.DivisionCreateSchema import DivisionCreateSchema

    from app.modules.hr.models.employee import Employee
    from app.modules.hr.schemas.employee import EmployeeCreateSchema

    from app.modules.machine.models import Machine
    from app.modules.machine.schemas.machine import MachineCreateSchema

    from app.modules.articles.models import Category, Unite
    from app.modules.articles.schemas.category import CategorySchema
    from app.modules.articles.schemas.unite import UniteSchema
    from app.modules.articles.models.marques import Marque
    from app.modules.articles.schemas.marques import MarqueSchema

    modifications = False

    # ------------------------------------------------------------------
    # Helper pour récupérer un objet sans faire crasher le script
    # ------------------------------------------------------------------
    def get_one_or_fail(query, description: str):
        instance = query.first()
        if not instance:
            print(f"[ERREUR FATALE] {description} introuvable en base de données !")

            # Récupération du modèle associé au query
            try:
                Model = query.column_descriptions[0]["entity"]
            except Exception:
                Model = None

            # Affichage du contenu de la table si possible
            if Model is not None:
                print(f"Contenu actuel de la table {Model.__tablename__} :")
                for obj in Model.query.all():
                    print(f"  → {obj}")
            else:
                print("Impossible de déterminer le modèle associé au query.")

            raise SystemExit(1)

        return instance


    # --- Sites ---
    site_data = [
        {
            "name": "BIOCHAMPS",
            "city": "LEZAT-SUR-LEZE",
            "country": "FRANCE",
            "address": "LACHET",
            "postal_code": "09210"
        }
    ]
    success = insert_if_empty(Site, SiteCreateSchema(), site_data, "sites", partial=False)
    modifications = modifications or success

    # Récupération sécurisée du site
    site_instance = get_one_or_fail(
        Site.query.filter_by(name="BIOCHAMPS"),
        "Site 'BIOCHAMPS'"
    )

    # --- Divisions (SERVICE) ---
    divisions_service_data = [
        {"site_id": site_instance.id, "type": "SERVICE", "name": "Production"},
        {"site_id": site_instance.id, "type": "SERVICE", "name": "Maintenance"},
        {"site_id": site_instance.id, "type": "SERVICE", "name": "R&D"},
    ]
    success = insert_if_empty(Division, DivisionCreateSchema(), divisions_service_data, "divisions (service)", partial=False)
    modifications = modifications or success


    # --- Divisions (DEPARTMENT) ---
    division_parent = get_one_or_fail(
        Division.query.filter_by(site_id=site_instance.id, name="Production", type="SERVICE"),
        "Division SERVICE 'Production'"
    )
    divisions_department_data = [
        {"site_id": site_instance.id, "parent_id": division_parent.id, "type": "DEPARTMENT", "name": "Fabrication"},
        {"site_id": site_instance.id, "parent_id": division_parent.id, "type": "DEPARTMENT", "name": "Suremballage"},
        {"site_id": site_instance.id, "parent_id": division_parent.id, "type": "DEPARTMENT", "name": "Expédition"},
    ]
    success = insert_if_empty(Division, DivisionCreateSchema(), divisions_department_data, "divisions (département)", partial=True)
    modifications = modifications or success


    # --- Divisions (ATELIER) ---
    division_parent = get_one_or_fail(
        Division.query.filter_by(site_id=site_instance.id, name="Fabrication", type="DEPARTMENT"),
        "Division DEPARTMENT 'Fabrication'"
    )
    divisions_atelier_data = [
        {"site_id": site_instance.id, "parent_id": division_parent.id, "type": "ATELIER", "name": "Atelier Animale"},
        {"site_id": site_instance.id, "parent_id": division_parent.id, "type": "ATELIER", "name": "Atelier Végétale"},
    ]
    success = insert_if_empty(Division, DivisionCreateSchema(), divisions_atelier_data, "divisions (ateliers)", partial=True)
    modifications = modifications or success


    # --- Divisions (LIGNES) : Atelier Végétale ---
    division_parent = get_one_or_fail(
        Division.query.filter_by(site_id=site_instance.id, name="Atelier Végétale", type="ATELIER"),
        "Division ATELIER 'Atelier Végétale'"
    )
    divisions_lignes_data = [
        {"site_id": site_instance.id, "parent_id": division_parent.id, "type": "LIGNE", "name": "Ligne Brassés Végétales"},
        {"site_id": site_instance.id, "parent_id": division_parent.id, "type": "LIGNE", "name": "Ligne Etuvés Végétales"},
    ]
    success = insert_if_empty(Division, DivisionCreateSchema(), divisions_lignes_data, "divisions (Lignes Végétales)", partial=True)
    modifications = modifications or success


    # --- Divisions (LIGNES) : Atelier Animale ---
    division_parent = get_one_or_fail(
        Division.query.filter_by(site_id=site_instance.id, name="Atelier Animale", type="ATELIER"),
        "Division ATELIER 'Atelier Animale'"
    )
    divisions_lignes_data = [
        {"site_id": site_instance.id, "parent_id": division_parent.id, "type": "LIGNE", "name": "Ligne Fromage Blanc"},
        {"site_id": site_instance.id, "parent_id": division_parent.id, "type": "LIGNE", "name": "Ligne Brassés Animale"},
        {"site_id": site_instance.id, "parent_id": division_parent.id, "type": "LIGNE", "name": "Ligne Etuvés Animale"},
        {"site_id": site_instance.id, "parent_id": division_parent.id, "type": "LIGNE", "name": "Ligne Crème Fraîche"},
        {"site_id": site_instance.id, "parent_id": division_parent.id, "type": "LIGNE", "name": "Ligne Faisselle"},
    ]
    success = insert_if_empty(Division, DivisionCreateSchema(), divisions_lignes_data, "divisions (Lignes Animales)", partial=True)
    modifications = modifications or success


    # --- Machines : Lignes Végétales ---
    division_parent = get_one_or_fail(
        Division.query.filter_by(site_id=site_instance.id, name="Ligne Brassés Végétales", type="LIGNE"),
        "Division LIGNE 'Ligne Brassés Végétales'"
    )
    machines_data = [
        {"site_id": site_instance.id, "division_id": division_parent.id, "name": "RI6", "type": "DOSEUSE", "model": "RI6", "serial_number": "201601010001", "manufacturer": "NOVA"},
    ]
    success = insert_if_empty(Machine, MachineCreateSchema(), machines_data, "machines (Ligne Brassés Végétales)", partial=False)
    modifications = modifications or success


    division_parent = get_one_or_fail(
        Division.query.filter_by(site_id=site_instance.id, name="Ligne Etuvés Végétales", type="LIGNE"),
        "Division LIGNE 'Ligne Etuvés Végétales'"
    )
    machines_data = [
        {"site_id": site_instance.id, "division_id": division_parent.id, "name": "PACKINOV", "type": "DOSEUSE", "model": "PACKINOV", "serial_number": "201601010002", "manufacturer": "NOVA"},
    ]
    success = insert_if_empty(Machine, MachineCreateSchema(), machines_data, "machines (Ligne Etuvés Végétales)", partial=False)
    modifications = modifications or success


    # --- Machines : Lignes Animales ---
    # Fromage Blanc
    division_parent = get_one_or_fail(
        Division.query.filter_by(site_id=site_instance.id, name="Ligne Fromage Blanc", type="LIGNE"),
        "Division LIGNE 'Ligne Fromage Blanc'"
    )
    machines_data = [
        {"site_id": site_instance.id, "division_id": division_parent.id, "name": "ERECAM", "type": "DOSEUSE", "model": "ERECAM", "serial_number": "201601010003", "manufacturer": "ERECAM"},
    ]
    success = insert_if_empty(Machine, MachineCreateSchema(), machines_data, "machines (Ligne Fromage Blanc)", partial=False)
    modifications = modifications or success


    # Brassés Animale
    division_parent = get_one_or_fail(
        Division.query.filter_by(site_id=site_instance.id, name="Ligne Brassés Animale", type="LIGNE"),
        "Division LIGNE 'Ligne Brassés Animale'"
    )
    machines_data = [
        {"site_id": site_instance.id, "division_id": division_parent.id, "name": "RI8", "type": "DOSEUSE", "model": "NOVA", "serial_number": "201601010004", "manufacturer": "NOVA"},
    ]
    success = insert_if_empty(Machine, MachineCreateSchema(), machines_data, "machines (Ligne Brassés Animale)", partial=False)
    modifications = modifications or success


    # Etuvés Animale
    division_parent = get_one_or_fail(
        Division.query.filter_by(site_id=site_instance.id, name="Ligne Etuvés Animale", type="LIGNE"),
        "Division LIGNE 'Ligne Etuvés Animale'"
    )
    machines_data = [
        {"site_id": site_instance.id, "division_id": division_parent.id, "name": "ERECAM2", "type": "DOSEUSE", "model": "ERECAM", "serial_number": "201601010005", "manufacturer": "ERECAM"},
    ]
    success = insert_if_empty(Machine, MachineCreateSchema(), machines_data, "machines (Ligne Etuvés Animale)", partial=False)
    modifications = modifications or success

    
    # --- Employés ---
    #=================================================================
    #                         --- EMPLOYES ---
    #=================================================================
    employee_data = [
        {"first_name": "Jacques", "last_name": "PY", "hire_date": "1986-10-01", "termination_date": "2016-12-01", "matricule": "1"},
        {"first_name": "Marie-José", "last_name": "Collignon", "hire_date": "1986-10-01", "termination_date": "2016-12-01", "matricule": "2"},
        {"first_name": "Jean-Frederic", "last_name": "AUGOYAT", "hire_date": "2003-03-01", "matricule": "3"},
        {"first_name": "Thierry", "last_name": "Renard", "hire_date": "2016-10-01", "termination_date": "2022-02-01", "matricule": "4"},
        {"first_name": "Jan", "last_name": "Roest Crollius", "hire_date": "2016-10-01", "matricule": "5"},
        {"first_name": "Caroline", "last_name": "ROEST", "hire_date": "2017-01-02", "matricule": "6"},
        {"first_name": "Camille", "last_name": "MARCELEAUD", "hire_date": "2022-08-01", "matricule": "7"},
        {"first_name": "Alain", "last_name": "leclerc", "hire_date": "2022-10-01", "termination_date": "2025-06-01", "matricule": "8"},
        {"first_name": "Audrey", "last_name": "CLAVEAU", "hire_date": "2024-01-02", "matricule": "9"},
        {"first_name": "Damien", "last_name": "VACILOTTO", "hire_date": "2024-01-02", "matricule": "10"},
    ]
    success = insert_if_empty(Employee, EmployeeCreateSchema(), employee_data, "employés", partial=False)
    modifications = modifications or success

    # --- Catégories d'articles ---
    article_types_data = [
        {"code": "MP", "name": "Matière première", "description": "Matières premières utilisées dans la production des articles finis."},
        {"code": "CF", "name": "Consommables / Fournitures", "description": "Articles utilisés dans le processus de production mais qui ne font pas partie du produit final."},
        {"code": "PF", "name": "Produit fini", "description": "Articles finis prêts à être vendus aux clients."},
        {"code": "PSF", "name": "Semi-fini", "description": "Articles nécessitant une ou plusieurs opérations avant d'être finis."},
        {"code": "EMB", "name": "Emballage", "description": "Matériaux d'emballage utilisés pour protéger et présenter les produits finis."},
        {"code": "DIV", "name": "Divers", "description": "Articles divers qui ne rentrent pas dans les autres catégories."},
    ]
    success = insert_if_empty(Category, CategorySchema(), article_types_data, "catégories d'articles", partial=False)
    modifications = modifications or success

    # --- Unités ---
    unite_data = [
        {"code": "g/100L", "libelle": "gramme/100Litre", "type_unite": "concentration", "description": "Unité de concentration massique, exprimant la masse d'une substance pour 100 litres de solution."},
        {"code": "g/L", "libelle": "gramme/Litre", "type_unite": "concentration", "description": "Unité de concentration massique, exprimant la masse d'une substance par litre de solution."},
        {"code": "L", "libelle": "Litre", "type_unite": "volume", "description": "Unité de volume utilisée pour le lait et les autres liquides."},
        {"code": "Kg", "libelle": "Kilogramme", "type_unite": "poids", "description": "Unité de masse utilisée pour les ingrédients solides et les emballages."},
        {"code": "g", "libelle": "Gramme", "type_unite": "poids", "description": "Sous-unité du kilogramme pour mesurer de petites quantités."},
        {"code": "PIECE", "libelle": "Pièce", "type_unite": "comptage", "description": "Unité utilisée pour compter les articles individuels comme les pots ou bouteilles."},
        {"code": "COLIS", "libelle": "Colis", "type_unite": "conditionnement", "description": "Unité correspondant à un carton regroupant plusieurs pièces."},
        {"code": "PALETTE", "libelle": "Palette", "type_unite": "logistique", "description": "Unité logistique correspondant à un ensemble de colis prêts pour l’expédition."},
    ]
    success = insert_if_empty(Unite, UniteSchema(), unite_data, "unités", partial=False)
    modifications = modifications or success

    # --- Marques ---
    marque_data = [
        {"nom": "Biochamps MSP", "description": "Marque spécialisée dans les produits laitiers biologiques."},
        {"nom": "Biochamps RHF", "description": "Marque spécialisée dans les produits laitiers biologiques pour RHF."},
        {"nom": "PROTT", "description": "Marque locale offrant une gamme de produits frais et naturels pour sportifs."},
        {"nom": "Les Près D'Ariège", "description": "Artisan du soja depuis 1994, proposant des alternatives végétales de qualité."},
        {"nom": "Laiterie des Pyrénées", "description": "Producteur de fromages et produits laitiers traditionnels des Pyrénées."},
        {"nom": "Biocoop", "description": "Chaîne de magasins spécialisée dans les produits biologiques et équitables."},
        {"nom": "La Vie Claire", "description": "Enseigne dédiée aux produits biologiques, naturels et diététiques."},
        {"nom": "Naturalia", "description": "Chaîne de magasins bio proposant une large gamme de produits naturels."},
        {"nom": "MORICE", "description": "Marque reconnue pour ses produits laitiers traditionnels et innovants."},
        {"nom": "Vif", "description": "Marque proposant des produits laitiers frais et de qualité."},
        {"nom": "Bonneterre", "description": "Marque engagée dans la production de produits biologiques et équitables."},
    ]
    success = insert_if_empty(Marque, MarqueSchema(), marque_data, "marques", partial=False)
    modifications = modifications or success

    # ===================================================================
    if modifications:
        print("[SUCCÈS] Base initialisée avec succès")
    else:
        print("[INFO] Aucune modification apportée à la base")