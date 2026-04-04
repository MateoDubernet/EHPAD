# Utilisation de l'image Python officielle 3.12 (basée sur Debian pour mysqlclient)
FROM python:3.12-slim

# Empêche Python de générer des fichiers .pyc et force l'affichage des logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installation des dépendances système nécessaires pour mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Mise à jour de pip et installation des dépendances mentionnées dans ton README
RUN pip install --upgrade pip
RUN pip install django mysqlclient

# Copie du reste du projet
COPY . .

# Exposition du port par défaut de Django
EXPOSE 8000

# Commande de lancement (on utilise le serveur de dev pour cette démo)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]