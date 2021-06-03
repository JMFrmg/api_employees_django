from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employees import views

# Routes de notre API
#Utilisation du routeur fourni par le framework Django_rest
#Les routes sont générées automatiquement pour du CRUD
# 5 routes sont générées pour chaque viewset du view.py de notre application :
# - une route pour lister toutes les entrées dans la base (requête : méthode HTTP GET)
# - http://<mon_url>/employees/  method http : GET
# - une route pour ajouter une entrée dans la base
# http://<mon_url>/employees/  method http : POST
# - une route pour lire une seule entrée de la base de données
# http://<mon_url>/employees/<id>  method http : GET
# - une route puur modifier une entrée
# http://<mon_url>/employees/<id>  method http : PATCH
# - une route pour supprimer une entrée
# GET http://<mon_url>/employees/<id>  method http : DELETE
router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)
router.register(r'departments', views.DepartmentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
    path("populate/", views.populate, name="populate")
]