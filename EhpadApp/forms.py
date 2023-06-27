from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

#Formulaire création de compte
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User #Définie le modele sur lequel se calque le formulaire
        fields = ('username', 'first_name', 'last_name',) #Définie les champs du formulaire