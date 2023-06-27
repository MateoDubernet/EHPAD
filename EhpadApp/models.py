from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.

username_validator = UnicodeUsernameValidator()

#Table CustomUser de la base de donnée
class CustomUser(AbstractUser):
        
    username = models.CharField(("username"),max_length=150,unique=True,help_text=(
        "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
    ), 
    validators=[username_validator],
    error_messages={"unique": ("A user with that username already exists."),},
    )
    first_name = models.CharField(("first name"), max_length=150, blank=True)
    last_name = models.CharField(("last name"), max_length=150, blank=True)
        
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
class Visitor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=200)
    message = models.TextField()