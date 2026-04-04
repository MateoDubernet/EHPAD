# EHPAD App

## Présentation
Il s'agit d'un projet Python réaliser en groupe durant mon alternance dans le cadre d'un devoir maison. Cette application est une **démo de site web** pour présenter un établissement EHPAD, incluant des fonctionnalités de gestion d'utilisateurs et de communication.

### Architecture
- **Backend** : Django.

- **Base de données** : MySQL.

- **Infrastructure** : Entièrement conteneurisé avec Docker pour un déploiement "zéro configuration".

---

## Installation & Lancement
### 1. Clonage du dépôt
```bash
    git clone https://github.com/MateoDubernet/EHPAD.git
```

### 2. Lancement (Docker)
**Prérequis :** [Docker Desktop](https://www.docker.com/products/docker-desktop) installé et lancé.

```bash
    cd ./EHPAD
    docker-compose up --build
```

### 3. Initialiser la base de données
```bash
    docker-compose exec web python manage.py migrate
```

### 4. Accès
- **Site Web** : http://localhost (Port 80)

---

## Fonctionnalités
L'application intègre un formulaire de contact. Par défaut, pour faciliter les tests sans configuration SMTP complexe, les emails sont envoyés vers la console Docker.
**Pour tester** : Envoyez un message via le formulaire et surveillez les logs dans votre terminal docker-compose. Le contenu du mail s'y affichera en texte brut.
