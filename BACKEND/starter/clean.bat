@echo off
REM BACKEND\clean.bat
REM ===============================
REM  Full clean of backend
REM ===============================

cd /d "%~dp0..\..\BACKEND"

echo [CLEAN] Removing virtual environment...
if exist venv (
    rmdir /s /q venv
    echo [OK] venv removed
) else (
    echo [INFO] No venv found
)

echo [CLEAN] Removing __pycache__ folders...
for /d /r . %%d in (__pycache__) do (
    if exist "%%d" (
        rmdir /s /q "%%d"
        echo [OK] Removed: %%d
    )
)

echo [CLEAN] Removing content of instance folder...
if exist instance (
    rmdir /s /q instance
    mkdir instance
    echo [OK] instance cleaned
) else (
    echo [INFO] No instance folder found
)

echo [CLEAN] Removing old migrations...
if exist migrations (
    rmdir /s /q migrations
    echo [OK] migrations removed
) else (
    echo [INFO] No migrations folder found
)

echo [DONE] Full clean finished !
pause
