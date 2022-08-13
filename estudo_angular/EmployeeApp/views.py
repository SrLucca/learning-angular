from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departament, Employees
from EmployeeApp.serializers import DepartamentSerializer, EmployeesSerializer
# Create your views here.

@csrf_exempt
def departamentApi(request, id=0):
    if request.method == 'GET':
        departaments = Departament.objects.all()
        departaments_serializer = DepartamentSerializer(departaments, many=True)
        return JsonResponse(departaments_serializer.data, safe=False)

    elif request.method == 'POST':
        departament_data = JSONParser().parse(request)
        departament_serializer = DepartamentSerializer(data=departament_data)
        if departament_serializer.is_valid():
            departament_serializer.save()
            return JsonResponse("Adicionado com Sucesso!!", safe=False)
        return JsonResponse("Falha ao Adiconar.", safe=False)
    
    elif request.method == 'PUT':
        departament_data = JSONParser().parse(request)
        departament = Departament.objects.get(pk=departament_data['id'])
        departament_serializer = DepartamentSerializer(departament, data=departament_data)
        if departament_serializer.is_valid():
            departament_serializer.save()
            return JsonResponse("Atualizacao realizada com Sucesso!!", safe=False)
        return JsonResponse("Erro na Atualizacao", safe=False)
    
    elif request.method == 'DELETE':
        departament = Departament.objects.get(pk=id)
        departament.delete()
        return JsonResponse("Deletado com Sucesso!!", safe=False)
        

@csrf_exempt
def employeesApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeesSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeesSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Adicionado com Sucesso!!", safe=False)
        return JsonResponse("Falha ao Adiconar.", safe=False)
    
    elif request.method == 'PUT':
        employees_data = JSONParser().parse(request)
        employees = Employees.objects.get(pk=employees_data['id'])
        employees_serializer = EmployeesSerializer(employees, data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Atualizacao realizada com Sucesso!!", safe=False)
        return JsonResponse("Erro na Atualizacao", safe=False)
    
    elif request.method == 'DELETE':
        employees = Employees.objects.get(pk=id)
        employees.delete()
        return JsonResponse("Deletado com Sucesso!!", safe=False)
        
