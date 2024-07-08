from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, "entidades/index.html")

def hosts(request):
     contexto = {"hosts": Hosts.objects.all()}
     return render(request, "entidades/hosts.html", contexto)

def vlans(request):
    contexto = {"vlans": Vlans.objects.all()}
    return render(request, "entidades/vlans.html", contexto)

def estudiantes(request):
    return render(request, "entidades/estudiantes.html")

def entregables(request):
    return render(request, "entidades/entregables.html")