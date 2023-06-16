"""
URL configuration for Projet_intégrateur project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accueil import views as accueil_views
from A_propos import views as apropos_views
from Connexion import views as connexion_views
from Contact import views as contact_views
from Inscription import views as inscription_views
from Page_de_choix import views as choix_views
from Page_de_visualisation import views as visualisation_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/', accueil_views.index,name='accueil'),
    path('A_propos/', apropos_views.A_propos),
    path('Connexion/', connexion_views.Connexion,name='Connexion'),
    path('Contact/', contact_views.Contact , name='Contact'),
    path('Inscription/', inscription_views.Inscription),
    path('Page_de_choix/', choix_views.Choix),
    path('Page_de_visualisation/', visualisation_views.Visualisation , name='Page_de_visualisation'),
]

