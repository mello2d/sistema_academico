from myapp.forms import ProfessorForm
from myapp.models import Professor 
from django.shortcuts import render, redirect

# Create your views here.
#
def index(request):
    return render(request, "lista.html")

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
    return render (request, '', {'form': form})

def alterarProfessor(request, id):
    professor = Professor.objects.get(id=id)
    if request.method == "POST":
        form = ProfessorForm(request.POST, isinstance = professor)
        if form.is_valid():
            form.save()
            return redirect('listar_professor')
    form = ProfessorForm(isinstance = professor)
    return render(request, "", {'form': form})

def excluirProfessor(request,id):
    professor = Professor.object.get(id=id)
    try:
        professor.delete()
    except:
        pass
    return redirect("listar_professor")