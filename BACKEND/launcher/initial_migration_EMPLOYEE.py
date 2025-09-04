# BACKEND\launcher\initial_migration_EMPLOYEE.py

from app import create_app

from .launcher_service import insert_if_empty  

from app.modules.hr.models.employee import Employee
from app.modules.hr.schemas.employee import EmployeeCreateSchema

# Import des modèles et schémas

app = create_app()

print("[COLD START] - Peuplement de la base de données")

with app.app_context():
    modifications = False

    # --- EMPLOYEE ---
    employee_data = [
    {"first_name": "Jacques", "last_name": "PY", "hire_date": "1986-10-01", "termination_date": "2016-12-01", "matricule": 1},
    {"first_name": "Marie-José", "last_name": "Collignon", "hire_date": "1986-10-01", "termination_date": "2016-12-01", "matricule": 2},
    {"first_name": "Jean-Frederic", "last_name": "AUGOYAT", "hire_date": "2003-03-01", "matricule": 3},
    {"first_name": "Thierry", "last_name": "Renard", "hire_date": "2016-10-01", "termination_date": "2022-02-01", "matricule": 4},
    {"first_name": "Jan", "last_name": "Roest Crollius", "hire_date": "2016-10-01", "matricule": 5},
    {"first_name": "Caroline", "last_name": "ROEST", "hire_date": "2017-01-02", "matricule": 6},
    {"first_name": "Camille", "last_name": "MARCELEAUD", "hire_date": "2022-08-01", "matricule": 7},
    {"first_name": "Alain", "last_name": "leclerc", "hire_date": "2022-10-01", "termination_date": "2025-06-01", "matricule": 8},
    {"first_name": "Audrey", "last_name": "CLAVEAU", "hire_date": "2024-01-02", "matricule": 9},
    {"first_name": "Damien", "last_name": "nonconnu", "hire_date": "2024-01-02", "matricule": 10},
]

    try:
        success = insert_if_empty(Employee, EmployeeCreateSchema(), employee_data, "Employee", False)
        modifications = modifications or success
    except Exception as e:
        print(f"[ERREUR] Échec de l'insertion des sites : {e}")
        import traceback
        traceback.print_exc()

    if modifications:
        print("[INFO] Base initialisée avec succès")
    else:
        print("[INFO] Aucune modification apportée à la base")
