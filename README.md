# EHPAD App

## Contexte

### Description
Il s'agit d'un projet Python réaliser en groupe durant mon alternance dans le cadre d'un devoir maison.
Cette application est une **démo de site web** pour présenter un EHPAD.  
Elle inclut deux fonctionnalités principales :  
- Un **formulaire de contact** (envoi d’email).  
- Un système d’**inscription et connexion utilisateur**.

---

## Prérequis

- Python
- Pip
- MySQL

---

## Installation & Lancement
### 1. Cloner le projet
```bash
    git clone https://github.com/MateoDubernet/EHPAD.git
```

### 2. Aller sur le projet
```bash
    cd EHPAD
```

### 3. Activer l’environnement virtuel
```bash
    .\EhpadEnv\Scripts\activate
```

### 4. Installer les dépendances
```bash
    python -m venv EhpadEnv
```
```bash
    python -m pip install --upgrade pip
```
```bash
    python -m pip install django
``` 
```bash
    pip install mysqlclient
```

### 5. Creer la base de donnée 'ehpad_project' manuellement

### 6. Changer les param de la base de donnée(port, user, mdp, host, port) dans Ehpad/setting.py -> DATABASES

### 7. Migrations
```bash
    python manage.py makemigrations
```
```bash
    python manage.py migrate
```

### 8. Configuration des emails
L’application utilise send_mail de Django pour envoyer les messages du formulaire de contact.

1. Modifier settings.py\
Ouvrir Ehpad/settings.py et configurer un serveur SMTP :
```bash
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.votre_service_mail.com"    # ex: smtp.gmail.com, smtp.sendinblue.com
    EMAIL_PORT = 587                               # ou 465 selon le service
    EMAIL_USE_TLS = True                           # ou EMAIL_USE_SSL = True
    EMAIL_HOST_USER = "votre_adresse@mail.com"    # adresse de l'expéditeur
    EMAIL_HOST_PASSWORD = "votre_mot_de_passe"    # mot de passe ou mot de passe application
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```
ou tester en local sans serveur SMTP, en utilisant le backend console :
```bash
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```
Les mails s’afficheront alors dans la console Django au lieu d’être envoyés réellement.

2. Vérifier le fichier views.py -> send_mail()\
Ouvrir EhpadApp/views.py et modifier recipient_list dans send_mail() si besoin, cela permet d'indiquer la liste des destinataires.

### 9. Lancer l'applicarion
```bash
    python manage.py runserver
```
Aller à l'adresse indiquer dans le terminal

---

## Fonctionnalités

### Formulaire de contact
1. Compléter le formulaire et valider
2. Aller à l'adresse mail configurer indiquer dans recipient_list pour voir le mail ou celle mis dans settings.py en fonction du serveur smtp utiliser
3. Vous avez maintenant accès aux emails envoyer depuis le formulaire

### Inscription et connexion
1. Créer un compte
2. Connecter-vous
