from django.db import models

# Create your models here.

class carroModel(models.Model):

    marca = models.CharField(max_length=255, blank = False, null=False)
    modelo = models.CharField(max_length=255, blank = False, null=False)
    ano = models.CharField(max_length=255, blank = False, null=False)
    qtd_donos = models.CharField(max_length=255, blank = False, null=False)
    preco = models.IntegerField(default=1000)

    def __str__(self):

        return self.modelo