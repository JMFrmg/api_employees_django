from employees.models import Employee, Department
from django.contrib.auth.models import User
from employees.serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework import permissions
from rest_framework import viewsets
from django.http import HttpResponse

# Utilisation des viewsets fournis par Django_rest
# Chaque viewset gère tous les aspects du CRUD pour une table de notre base de données.
# Il est aussi possible de le coder manuellement sans utiliser les objets Django_rest
# ex:
# pour récupérer l'ensemble des entrées d'une table et les renvoyer au template :
# def get_employees(request):
#     employees = Employee.objects.all()
#     return render(request, <mon_template>, employees)
# pour supprimer une entrée dans la BDD :
# def rm_employee(request, id):
#     employee = Employee.objects.get(pk=id)
#     employee.delete()
# ...
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# vue qui permet de peupler la BDD
# url : http://<mon_url>/populate
def populate(request):
    if request.user.is_superuser:
        import pandas as pd
        from random import randint

        df = pd.read_csv("employees/full_names.csv")
        all_departments = Department.objects.all()
        all_users = User.objects.all()
        for r in df.iterrows():
            cities = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Montpellier", "Strasbourg", "Bordeaux"]
            positions = ["employé", "cadre", "cadre sup", "dirigeant"]
            n = 0
            while n < 5:
                try:
                    new_employee = Employee(first_name=r[1][0],
                                            last_name=r[1][1],
                                            current=True,
                                            age=randint(18, 65),
                                            city= cities[randint(0, len(cities)-1)],
                                            position=positions[randint(0, len(positions)-1)],
                                            salary=randint(20000, 100000),
                                            department=all_departments[randint(0, len(all_departments)-1)],
                                            department_chief=all_users[randint(0, len(all_users)-1)])
                    new_employee.save()
                    break
                except:
                    n += 1
                    continue
        print(df.shape)
    else:
        return HttpResponse('Unauthorized', status=401)