
from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name="home"),
    path('hosts/', hosts, name="hosts"),
    path('vlans/', vlans, name="vlans"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
]
