from rest_framework import serializers
from employees.models import Employee, Department
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    department_chief = serializers.ReadOnlyField(source='department_chief.username')

    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "full_name", "hired", "current", "age", "city", "position", "salary", "department", "department_chief"]

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    employees = serializers.HyperlinkedRelatedField(many=True, view_name='employee-detail', read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'floor', 'employees']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    employees = serializers.HyperlinkedRelatedField(many=True, view_name='employee-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'employees']