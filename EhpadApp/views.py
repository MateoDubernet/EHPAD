from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from . forms import *
from . models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.

#permet de créer un utilisateur
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() #Enregistre un nouvelle utilisateur

            # Récupére les données du formulaire
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password) #Vérifie le nom de l'utilisateur et le mot de passe correspondent

            login(request, user)
            return redirect("EhpadApp:home")
        else:
            return render(request, 'EhpadApp/register.html', {'form': form})
    else:
        form = CustomUserCreationForm() #Formulaire de création d'utilisateur
        return render(request, 'EhpadApp/register.html', {'form': form})

#permet de se connecter
def logIn(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Récupére les données du formulaire
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Vérifie le nom de l'utilisateur et le mot de passe correspondent
            user = authenticate(username=username, password=password) 
            if user is not None:
                login(request, user)
                return redirect("EhpadApp:home")
            else:
                return render(request, 'EhpadApp/login.html', {'form': form, 'erreur': "Nom d'utilisateur ou mot de passe incorrect."})
        else:
            return render(request, 'EhpadApp/login.html', {'form': form, 'erreur': "Nom d'utilisateur ou mot de passe incorrect."})
    else:
        form = AuthenticationForm() #Formulaire d'authentification d'utilisateur
        return render(request, 'EhpadApp/login.html', {'form': form})

#permet de se déconnecter
def logOut(request):
    logout(request)
    return redirect("EhpadApp:home")

#affiche la page home
def home(request):
    return render(request, 'EhpadApp/home.html', {'user': request.user})

#affiche la page about
def about(request):
    return render(request, 'EhpadApp/about.html')

#affiche la page services
def services(request):
    return render(request, 'EhpadApp/services.html')

#affiche la page faq
def faq(request):
    return render(request, 'EhpadApp/faq.html')

#affiche la page visit
def visite(request):
    return render(request, 'EhpadApp/visite.html')

#formulaire de contact
def visitor_contact_form(request):
    if request.method == 'POST':
        form = VisitorContactForm(request.POST)
        if form.is_valid():
            form.save() 

            # Récupére les données du formulaire
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            #Récupére la page email
            html = render_to_string('EhpadApp/email.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
            })

            #Envoie un email à l'adresse: projetdjango3@gmail.com
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['projetdjango3@gmail.com'],
                html_message=html
            )

            return redirect('EhpadApp:contact')
        else: 
            return render(request, 'EhpadApp/contact.html', {'form': form})
    else:
        # Renvoie la page contact avec un formulaire vide
        form = VisitorContactForm()
        return render(request, 'EhpadApp/contact.html', {'form': form})




    
