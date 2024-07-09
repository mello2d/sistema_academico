from django.shortcuts import render, redirect

from myapp.forms import AlunoForm
from myapp.models import Aluno
from myapp.forms import CursoForm, ProfessorForm
from myapp.models import Curso, Professor

# Create your views here.
def listarAluno(request):

    aluno = Aluno.objects.order_by('nome')
    return render(request, 'aluno/lista.html',{'aluno': aluno}) 
    
def incluirAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_aluno')
    form = AlunoForm()
    return render(request, 'aluno/form_aluno.html', {'form': form})

def alterarAluno(request, id):
     aluno = Aluno.objects.get(id = id) #get - buscando o cliente por id 
     if request.method ==  'POST':
        form = AlunoForm(request.POST, instance = aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_aluno')
     form = AlunoForm(instance = aluno)
     return render(request, 'aluno/form_aluno.html', {'form': form})

def excluirAluno(request, id):
    veiculo = Aluno.objects.get (id = id)
    try:
     veiculo.delete()
    except:
      pass    
    return redirect('listar_aluno')

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

