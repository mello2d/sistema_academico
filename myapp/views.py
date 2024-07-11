from django.shortcuts import render, redirect
from myapp.models import Aluno, Curso, Professor,Turma
from myapp.forms import AlunoForm, CursoForm, ProfessorForm, TurmaForm
from django.contrib import messages

# Create your views here.

# Index


def index(request):
    return render(request, "index.html")

# Alunos


def listarAluno(request):

    aluno = Aluno.objects.order_by('nome')
    return render(request, 'aluno/lista.html', {'aluno': aluno})


def incluirAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_aluno')
    form = AlunoForm()
    return render(request, 'aluno/form_aluno.html', {'form': form})


def alterarAluno(request, id):
    aluno = Aluno.objects.get(id=id)  # get - buscando o cliente por id
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_aluno')
    form = AlunoForm(instance=aluno)
    return render(request, 'aluno/form_aluno.html', {'form': form})


def excluirAluno(request, id):
    veiculo = Aluno.objects.get(id=id)
    try:
        veiculo.delete()
    except:
        pass
    return redirect('listar_aluno')

# Professores


def listarProfessor(request):
    professor = Professor.objects.order_by('nome')
    return render(request, 'professor/lista.html', {'professor': professor})


def incluirProfessor(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_professor')
    form = ProfessorForm()
    return render(request, 'professor/form_professor.html', {'form': form})


def alterarProfessor(request, id):
    professor = Professor.objects.get(id=id)
    if request.method == "POST":
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('listar_professor')
    form = ProfessorForm(instance=professor)
    return render(request, "professor/form_professor.html", {'form': form})


def excluirProfessor(request, id):
    professor = Professor.objects.get(id=id)
    try:
        professor.delete()
    except:
        pass
    return redirect("listar_professor")

# Listar cursos


def listarCursos(request):
    cursos = Curso.objects.order_by('nome')
    return render(request, 'cursos/lista.html', {'cursos': cursos})

# Incluir curso


def incluirCurso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')

    form = CursoForm()
    return render(request, 'cursos/form_curso.html', {'form': form})


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
        messages.error(request, "Não foi possível excluir devido a associações.")

    return redirect('listar_cursos')

def listarTurmas(request):
    turma = Turma.objects.order_by('curso')

    return render(request, 'turma/lista.html', {'turma': turma})

def incluirTurma(request):
    if request.method == "POST":
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_turmas')

    form = TurmaForm()
    return render(request, 'turma/form_turma.html', {'form': form})

def alterarTurma(request, id):
    turma = Turma.objects.get(id=id)

    if request.method == "POST":
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            return redirect('listar_turmas')

    form = TurmaForm(instance=turma)
    return render(request, 'turma/form_turma', {'form': form})

def excluirTurma(request, id):
    turma = Turma.objects.get(id=id)

    try:
        turma.delete()

    except:
        pass

    return redirect('listar_turmas')