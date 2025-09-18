A. Lancer l'application :

    1. lancer la commande: .\EhpadEnv\Scripts\activate

    2. installer Django sur EhpadEnv: 
        - python -m pip install --upgrade pip
        - python -m pip install django

    3. installer mysqlclient: pip install mysqlclient

    4. creer la base de donnée 'ehpad_project' manuellement

    5. changer les param de la base de donnée(port, user, mdp, host, port) dans Ehpad/setting.py

    6. Lancer la commande: python manage.py makemigrations

    7. Ensuite la commande: python manage.py migrate

    8. Lancer l'applicarion: python manage.py runserver

    9. Aller à l'adresse: 127.0.0.1:8000

B. Formulaire de contact

## Configuration des emails
Pour que l’envoi d’emails fonctionne, il faut modifier le fichier settings.py et éventuellement views.py si nécessaire.

1. Modifier settings.py\
Ouvreir Ehpad/settings.py et configure un serveur SMTP :
```bash
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.votre_service_mail.com"    # ex: smtp.gmail.com, smtp.sendinblue.com
    EMAIL_PORT = 587                               # ou 465 selon le service
    EMAIL_USE_TLS = True                           # ou EMAIL_USE_SSL = True
    EMAIL_HOST_USER = "votre_adresse@mail.com"    # adresse de l'expéditeur
    EMAIL_HOST_PASSWORD = "votre_mot_de_passe"    # mot de passe ou mot de passe application
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```
Pour tester en local sans serveur SMTP, il est possible d'utiliser le backend console :
```bash
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```
Les mails s’afficheront alors dans la console Django au lieu d’être envoyés réellement.

2. Vérifier le fichier views.py -> send_mail()
Dans recipient_list indiquer la liste des destinataires.

## Utilisation

    1. compléter le formulaire et valider

    2. aller sur le site: https://mailtrap.io/inboxes/2294690/messages

    3. connectez-vous avec les identifiants suivant:
        Email: projetDjango3@gmail.com
        Password: projetDjango3

    4. Vous avez maintenant accès aux emails envoyer depuis le formulaire

