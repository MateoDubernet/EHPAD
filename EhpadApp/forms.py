from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from . models import Visitor

User = get_user_model()

#Formulaire création de compte
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User #Définie le model sur lequel se calque le formulaire
        fields = ('username', 'first_name', 'last_name',) #Définie les champs du formulaire

class VisitorContactForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'email', 'subject', 'message']