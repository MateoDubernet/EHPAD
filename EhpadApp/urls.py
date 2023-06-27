from django.urls import path
from . import views

app_name = 'EhpadApp'
urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.logIn, name="login"),
    path("logout/", views.logOut, name="logout"),
    path("home/", views.home, name="home"),
    path("contact/", views.visitor_contact_form, name="contact"),
]