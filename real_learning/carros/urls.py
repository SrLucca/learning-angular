from django.urls import path, re_path
from carros import views


urlpatterns = [

    re_path(r'^carro/$', views.carrosAPI),
    re_path(r'^carro/([0-9]+)$', views.carrosAPI), #para visualizar ou editar um especifico
    
]