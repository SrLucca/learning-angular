from django.db import models

# Create your models here.

class Departament(models.Model):
    
    name = models.CharField(max_length=250) 

class Employees(models.Model):

    name = models.CharField(max_length=250) 
    departament_name = models.CharField(max_length=250) 
    date_joing = models.DateField()
    PhotoFileName = models.CharField(max_length=250) 