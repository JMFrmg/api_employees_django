"""
Le fichier model.py de l'application Django décrit la structure de la base de données
Chaque classe de la famille models.Model correspond à une table
Chaque variable au sein d'une classe correspond à une colonne
Les objects models.<...>Field nous permettent de créer les colonnes d'un certain type
et avec certains paramètres (ex:blank=True, default=<valeur> ...)
"""

from django.db import models

# Model department
class Department(models.Model):
    name = models.CharField(max_length=200)
    floor = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

#Model employee
class Employee(models.Model):
    hired = models.DateTimeField(auto_now_add=True)#date d'embauche
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.SmallIntegerField(default=30)
    city = models.CharField(max_length=200, default="paris")
    position = models.CharField(max_length=200, default="cadre")
    salary = models.IntegerField(default=30000)
    current = models.BooleanField(default=True)#current=True si la personne est actuellement toujours employée par l'entreprise
    department = models.ForeignKey(Department, related_name="employees", on_delete=models.RESTRICT)#ForeignKey qui renvoie la table department (relation oneToMany)
    owner = models.ForeignKey("auth.User", related_name="employees", on_delete=models.CASCADE)#owner=User qui a créé l'entrée dans la base

    # Fonction qui retourne le nom complet de l'employé avec les premières lettres en majuscules
    def full_name(self):
        return '%s %s' % (self.first_name.capitalize(), self.last_name.capitalize())

    # Le simple appel de l'objet sans aucune méthode renverra le nom complet de l'employé
    def __str__(self):
        return self.full_name()

    # Par défaut les réponses seront classées par date d'embauche
    class Meta:
        ordering = ['hired']