from django.shortcuts import render, redirect
from myapp.forms import CursoForm
from myapp.models import Curso

# Create your views here.

def listarCursos(request):
    curso = Curso.objects.order_by('nome')
    return render(request, 'cursos/lista.html', {'cursos': curso})

def incluirCurso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incluir_curso')

        form = CursoForm()
    return render(request, 'curso/form_curso.html', {'form': form})
