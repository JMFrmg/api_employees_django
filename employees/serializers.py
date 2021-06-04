from rest_framework import serializers
from employees.models import Employee, Department


# Serializer des object Employee
class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        # liste des champs :
        fields = ["id", "first_name", "last_name", "full_name", "hired", "current", "age", "city", "position", "salary", "department"]

    # On surcharge la méthode create de base :
    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        return employee

# Serializer des objets Department
class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        department = Department.objects.create(**validated_data)
        return department

