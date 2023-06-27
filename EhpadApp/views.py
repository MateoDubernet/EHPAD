from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from . forms import CustomUserCreationForm
from . models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.

#permet de créer un utilisateur
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() #Enregistre un nouvelle utilisateur
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
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) #Vérifie le nom de l'utilisateur et le mot de passe correspondent

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
@login_required()
def logOut(request):
    logout(request)
    return redirect("EhpadApp:login")

#affiche la page home
@login_required()
def home(request):
    return render(request, 'EhpadApp/home.html', {'user': request.user})




    
