from rest_framework import serializers
from EmployeeApp.models import Departament, Employees

class DepartamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departament
        fields = ('name')

class EmployeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = ('name', 'departament_name', 'date_joing','PhotoFileName')