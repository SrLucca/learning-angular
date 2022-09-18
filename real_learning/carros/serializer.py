from rest_framework import serializers
from carros.models import carroModel
from django.db.models import fields

class carroSerializer(serializers.ModelSerializer):

    class Meta:
        model = carroModel
        fields = ['marca', 'modelo', 'ano', 'qtd_donos', 'preco']