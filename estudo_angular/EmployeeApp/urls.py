from django.urls import path
from django.urls import include, re_path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #path(),
    re_path(r'^departament/$', views.departamentApi),
    re_path(r'^departament/([0-9]+)$', views.departamentApi),

    re_path(r'^employees/$', views.employeesApi),
    re_path(r'^employees/([0-9]+)$', views.employeesApi),

    re_path(r'^SaveFile$', views.saveFile),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)