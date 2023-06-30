A. Lancer l'application :

    1. lancer la commande: .\EhpadEnv\Scripts\activate

    2. installer Django sur EhpadEnv: pip install django

    3. installer mysqlclient: pip install mysqlclient

    4. creer la base de donnée 'ehpad_project' manuellement

    5. changer les param de la base de donnée(port, user, mdp, host, port) dans Ehpad/setting.py

    6. Lancer la commande: python manage.py makemigrations

    7. Ensuite la commande: python manage.py migrate

    8. Lancer l'applicarion: python manage.py runserver

    9. Aller à l'adresse: 127.0.0.1:8000

B. Formulaire de contact

    1. compléter le formulaire et valider

    2. aller sur le site: https://mailtrap.io/inboxes/2294690/messages

    3. connectez-vous avec les identifiants suivant:
        Email: projetDjango3@gmail.com
        Password: projetDjango3

    4. Vous avez maintenant accès aux emails envoyer depuis le formulaire

