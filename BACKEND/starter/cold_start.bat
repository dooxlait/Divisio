@echo off
REM BACKEND\starter.bat
REM ===============================
REM Start backend Flask with auto reload
REM + Create first migration and upgrade DB if needed
REM ===============================

REM --- Aller dans le dossier BACKEND ---
cd /d "%~dp0..\..\BACKEND"

REM --- Créer le virtual environment si inexistant ---
if not exist "venv" (
    echo [SETUP] Creating virtual environment...
    python -m venv venv
)

REM --- Activer le virtual environment ---
call venv\Scripts\activate.bat

REM --- Mettre à jour pip ---
echo [SETUP] Updating pip...
python -m pip install --upgrade pip

REM --- Installer les dépendances si requirements.txt existe ---
if exist "requirements.txt" (
    echo [SETUP] Installing dependencies...
    pip install -r requirements.txt
) else (
    echo [WARN] No requirements.txt found. Generating one...
    pip freeze > requirements.txt
)

REM --- Définir les variables d'environnement Flask ---
set FLASK_APP=run.py
set FLASK_ENV=development
set FLASK_DEBUG=1

REM --- Initialiser les migrations si nécessaire ---
if not exist "migrations" (
    echo [DB] Initializing migrations...
    flask db init
)

REM --- Générer la migration initiale ---
echo [DB] Generating migration...
flask db migrate -m "Initial migration"

REM --- Appliquer la migration à la base ---
echo [DB] Applying migration...
flask db upgrade

REM --- Initialisation de la base via initial_migration_FACTORY.py ---
IF EXIST "launcher\initial_migration.py" (
    echo [INFO] Initialisation de la base

    REM Activer l'environnement virtuel
    call venv\Scripts\activate.bat

    echo [INFO] Initialisation de la base FACTORY
    python -m launcher.initial_migration

) ELSE (
    echo [AVERTISSEMENT] launcher\initial_migrationpy introuvable. Etape passee.
)
    

REM --- Lancer Flask dans une nouvelle fenêtre avec auto reload ---
echo [START] Starting Flask server with auto reload...
start cmd /k "call venv\Scripts\activate.bat && flask run"

echo [DONE] Starter finished. All windows should be open.
pause
