from django.urls import path
from . import views
from django.views.generic.base import RedirectView

app_name = 'EhpadApp'
urlpatterns = [
    path("", RedirectView.as_view(url='home/'), name="empty"),
    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.logIn, name="login"),
    path("logout/", views.logOut, name="logout"),
    path("contact/", views.visitor_contact_form, name="contact"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
    path("faq/", views.faq, name="faq"),
    path("visite/", views.visite, name="visite"),
]