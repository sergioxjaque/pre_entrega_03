from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "entidades/home.html")

def cursos(request):
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)

def profesores(request):
    return render(request, "entidades/profesores.html")

def estudiantes(request):
    return render(request, "entidades/estudiantes.html")

def entregables(request):
    return render(request, "entidades/entregables.html")