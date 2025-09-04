@echo off
REM BACKEND\starter_hot.bat
REM ===============================
REM  Start backend Flask in a new window (with auto reload)
REM ===============================

REM Go to BACKEND folder (relative to this script)
cd /d "%~dp0..\..\BACKEND"

REM Activate venv
call venv\Scripts\activate.bat

REM Define Flask app (development + hot reload)
set FLASK_APP=run.py
set FLASK_ENV=development
set FLASK_DEBUG=1

REM Start Flask in a new window with auto reload
echo [START] Starting Flask server with auto reload in a new window...
start cmd /k "call venv\Scripts\activate.bat && flask run"
