FROM python:3.11-slim

WORKDIR /app

# Installer gcc pour les packages Python compilés
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Copier et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code
COPY . .

# Exposer le port Flask
EXPOSE 5000

# Variables d'environnement Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV FLASK_ENV=development

# Commande pour démarrer Flask
CMD ["flask", "run"]
