from django.contrib import admin
from django.urls import path, include

#Création du pattern du routes principal du projet
urlpatterns = [
    path('admin/', admin.site.urls),#route vers l'interface d'administration générée par Django
    path('', include("employees.urls")),#route vers l'application qui gère notre API d'employés
    path('api-auth/', include('rest_framework.urls')),#routes d'authentification
]
