from rest_framework import serializers
from employees.models import Employee, Department
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "full_name", "hired", "current", "age", "city", "position", "salary", "department"]

    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        return employee

class DepartmentSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'floor', 'employees']

    def create(self, validated_data):
        employees_data = validated_data.pop('employees')
        department = Department.objects.create(**validated_data)
        for employee_data in employees_data:
            Employee.objects.create(department=department, **employee_data)
        return department