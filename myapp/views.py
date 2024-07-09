from myapp.forms import CursoForm, ProfessorForm
from myapp.models import Curso, Professor
from django.shortcuts import render, redirect

# Create your views here.
#


def index(request):
    return render(request, "index.html")


def listarProfessor(request):
    professor = Professor.objects.order.by('nome')
    return render(request, '', {'professor': professor})


def incluirProfessor(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_professor')
    form = ProfessorForm()
    return render(request, '', {'form': form})


def alterarProfessor(request, id):
    professor = Professor.objects.get(id=id)
    if request.method == "POST":
        form = ProfessorForm(request.POST, isinstance=professor)
        if form.is_valid():
            form.save()
            return redirect('listar_professor')
    form = ProfessorForm(isinstance=professor)
    return render(request, "", {'form': form})


def excluirProfessor(request, id):
    professor = Professor.object.get(id=id)
    try:
        professor.delete()
    except:
        pass
    return redirect("listar_professor")

# alterar Curso


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
