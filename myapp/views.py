from django.shortcuts import render, redirect
from myapp.forms import CursoForm

from myapp.models import Curso

# Create your views here.

# Alterar curso


def alterarCurso(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')

    form = CursoForm(instance=curso)
    return render(request, 'cursos/form_curso.html', {'form': form})

# Excluir curso


def excluirCurso(request, id):
    curso = Curso.objects.get(id=id)

    try:
        curso.delete()

    except:
        pass

    return redirect('listar_cursos')
