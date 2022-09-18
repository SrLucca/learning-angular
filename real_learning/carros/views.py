from django.shortcuts import render
from carros.serializer import carroSerializer
from carros.models import carroModel

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.response import Response


# Create your views here.

@csrf_exempt
def carrosAPI(request, id=0):
    
    if request.method == 'GET':
        carros = carroModel.objects.all()
        carros_serializer = carroSerializer(carros, many=True)

        return JsonResponse(carros_serializer.data, safe=False)

    elif request.method == 'POST':
        carros_data = JSONParser().parse(request)
        carros_serializer = carroSerializer(data=carros_data)
        if carros_serializer.is_valid():
            carros_serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Erro ao adicionar", safe=False)

