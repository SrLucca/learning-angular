from django.urls import path
from django.urls import include, re_path
from EmployeeApp import views

urlpatterns = [
    #path(),
    re_path(r'^departament/$', views.departamentApi),
    re_path(r'^departament/([0-9]+)$', views.departamentApi),

    re_path(r'^employees/$', views.employeesApi),
    re_path(r'^employees/([0-9]+)$', views.employeesApi),

]