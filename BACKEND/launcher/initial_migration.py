# BACKEND\launcher\initial_migration.py
import time

from app import create_app
from .launcher_service import insert_if_empty  

# Import des modèles et schémas
from app.modules.factory.models.site import Site
from app.modules.factory.schemas.site.SiteCreateSchema import SiteCreateSchema

from app.modules.factory.models.division import Division
from app.modules.factory.schemas.division.DivisionCreateSchema import DivisionCreateSchema

from app.modules.hr.models.employee import Employee
from app.modules.hr.schemas.employee import EmployeeCreateSchema

from app.modules.machine.models import Machine
from app.modules.machine.schemas.machine import MachineCreateSchema

from app.modules.articles.models import Category
from app.modules.articles.schemas.category import CategorySchema

from app.modules.articles.models import Unite
from app.modules.articles.schemas.unite import UniteSchema


app = create_app()

print("[COLD START] - Peuplement de la base de données")

with app.app_context():
    modifications = False

    # --- Sites ---
    site_data = [
        {"name": "biochamps", "city": "LEZAT-SUR-LEZE", "country": "FRANCE", "address": "LACHET", "postal_code": "09210"}
    ]

    try:
        success = insert_if_empty(Site, SiteCreateSchema(), site_data, "sites", False)
        modifications = modifications or success
    except Exception as e:
        print(f"[ERREUR] Échec de l'insertion des sites : {e}")
        import traceback
        traceback.print_exc()

    # --- Divisions (rang service) ---
    site_instance = Site.query.filter_by(name="BIOCHAMPS").first()
    if site_instance:
        divisions_service_data = [
            {"site_id": site_instance.id, "type": "SERVICE", "name": "Production"},
            {"site_id": site_instance.id, "type": "SERVICE", "name": "Maintenance"},
            {"site_id": site_instance.id, "type": "SERVICE", "name": "R&D"},
        ]
        try:
            success = insert_if_empty(Division, DivisionCreateSchema(), divisions_service_data, "divisions (service)", False)
            modifications = modifications or success
        except Exception as e:
            print(f"[ERREUR] Échec de l'insertion des divisions (service) : {e}")
            import traceback
            traceback.print_exc()
    else:
        print("[WARN] Aucun site trouvé pour créer les divisions (service)")

    # --- Divisions (rang département) ---
    division_parent_instance = Division.query.filter_by(
        site_id=site_instance.id, name="Production", type="SERVICE"
    ).first()

    if division_parent_instance:
        divisions_department_data = [
            {"site_id": site_instance.id, "parent_id": division_parent_instance.id, "type": "DEPARTMENT", "name": "Fabrication"},
            {"site_id": site_instance.id, "parent_id": division_parent_instance.id, "type": "DEPARTMENT", "name": "Suremballage"},
            {"site_id": site_instance.id, "parent_id": division_parent_instance.id, "type": "DEPARTMENT", "name": "Expédition"},
        ]
        try:
            # Note : utilisation de la nouvelle fonction insert_if_not_exists
            success = insert_if_empty(Division, DivisionCreateSchema(), divisions_department_data, "divisions (department)", True)
            modifications = modifications or success
        except Exception as e:
            print(f"[ERREUR] Échec de l'insertion des divisions (department) : {e}")
            import traceback
            traceback.print_exc()
    else:
        print("[WARN] Aucun parent trouvé pour créer les divisions (department)")
    
    # --- Divisions (rang Atelier) ---
    division_parent_instance = Division.query.filter_by(
        site_id=site_instance.id, name="Fabrication", type="DEPARTMENT"
    ).first()

    if division_parent_instance:
        divisions_atelier_data = [
            {"site_id": site_instance.id, "parent_id": division_parent_instance.id, "type": "ATELIER", "name": "Atelier Animale"},
            {"site_id": site_instance.id, "parent_id": division_parent_instance.id, "type": "ATELIER", "name": "Atelier Vegetale"},
        ]
        try:
            # Note : utilisation de la nouvelle fonction insert_if_not_exists
            success = insert_if_empty(Division, DivisionCreateSchema(), divisions_atelier_data, "divisions (Ateliers)", True)
            modifications = modifications or success
        except Exception as e:
            print(f"[ERREUR] Échec de l'insertion des divisions (Ateliers) : {e}")
            import traceback
            traceback.print_exc()
    else:
        print("[WARN] Aucun parent trouvé pour créer les divisions (Ateliers)")

    # --- Machines  ---

    division_parent_instance = Division.query.filter_by(
        site_id=site_instance.id, name="Atelier Animale", type="ATELIER"
    ).first()

    if division_parent_instance:
        machines_data = [
            { "site_id": site_instance.id, "division_id": division_parent_instance.id, "name": "DOSEUSE 1", "type": "DOSEUSE", "model": "AXIA 1800", "serial_number": "201601010001", "manufacturer": "CONDINOV",},
            { "site_id": site_instance.id, "division_id": division_parent_instance.id, "name": "DOSEUSE 2", "type": "DOSEUSE", "model": "AXIA 1800", "serial_number": "201601010002", "manufacturer": "CONDINOV",},
            { "site_id": site_instance.id, "division_id": division_parent_instance.id, "name": "DOSEUSE 3", "type": "DOSEUSE", "model": "AXIA 1800", "serial_number": "201601010003", "manufacturer": "CONDINOV",},
        ]

        try:
            success = insert_if_empty(
                Machine, MachineCreateSchema(), machines_data, "machines (atelier animale)", False
            )
            modifications = modifications or success
        except Exception as e:
            print(f"[ERREUR] Échec de l'insertion des machines : {e}")
            import traceback
            traceback.print_exc()
    else:
        print("[WARN] Aucun parent trouvé pour créer les machines (atelier animale)")

    # --- EMPLOYEE ---
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

    try:
        success = insert_if_empty(Employee, EmployeeCreateSchema(), employee_data, "Employee", False)
        modifications = modifications or success
    except Exception as e:
        print(f"[ERREUR] Échec de l'insertion des sites : {e}")
        import traceback
        traceback.print_exc()

    # --- DIVISION_EMPLOYEE ---
    all_employee = Employee.query.all()

    employee_ids = [e.id for e in Employee.query.with_entities(Employee.id)]

    # --- CATEGORYS D'ARTICLE ---
    article_types_data = [
        {"code": "MP", "name": "Matière première", "description": "Matières premières utilisées dans la production des articles finis."},
        {"code": "CF", "name": "Consommables / Fournitures", "description": "Articles utilisés dans le processus de production mais qui ne font pas partie du produit final."},
        {"code": "PF", "name": "Produit fini", "description": "Articles finis prêts à être vendus aux clients."},
        {"code": "PSF", "name": "Produit semi fini", "description": "Articles necessitant une ou plusieurs opérations avant d'être finis."},
        {"code": "EMB", "name": "Emballage", "description": "Matériaux d'emballage utilisés pour protéger et présenter les produits finis."},
        {"code": "DIV", "name": "Divers", "description": "Articles divers qui ne rentrent pas dans les autres catégories."},
    ]

    try:
        success = insert_if_empty(Category, CategorySchema(), article_types_data, "categories", False)
        modifications = modifications or success
    except Exception as e:
        print(f"[ERREUR] Échec de l'insertion des catégories d'articles : {e}")
        import traceback
        traceback.print_exc()

    # --- UNITE D'ARTICLE ---
    unite_data = [
        {
            "code": "L",
            "libelle": "Litre",
            "type_unite": "volume",
            "description": "Unité de volume utilisée pour le lait et les autres liquides."
        },
        {
            "code": "KG",
            "libelle": "Kilogramme",
            "type_unite": "poids",
            "description": "Unité de masse utilisée pour les ingrédients solides et les emballages."
        },
        {
            "code": "G",
            "libelle": "Gramme",
            "type_unite": "poids",
            "description": "Sous-unité du kilogramme pour mesurer de petites quantités."
        },
        {
            "code": "PIECE",
            "libelle": "Pièce",
            "type_unite": "comptage",
            "description": "Unité utilisée pour compter les articles individuels comme les pots ou bouteilles."
        },
        {
            "code": "COLIS",
            "libelle": "Colis",
            "type_unite": "conditionnement",
            "description": "Unité correspondant à un carton regroupant plusieurs pièces."
        },
        {
            "code": "PALETTE",
            "libelle": "Palette",
            "type_unite": "logistique",
            "description": "Unité logistique correspondant à un ensemble de colis prêts pour l’expédition."
        },
    ]

    try:
        success = insert_if_empty(Unite, UniteSchema(), unite_data, "unités", False)
        modifications = modifications or success
    except Exception as e:
        print(f"[ERREUR] Échec de l'insertion des unités d'articles : {e}")
        import traceback
        traceback.print_exc()




    if modifications:
        print("[INFO] Base initialisée avec succès")
    else:
        print("[INFO] Aucune modification apportée à la base")
