from django.shortcuts import render, redirect

from myapp.forms import AlunoForm
from myapp.models import Aluno

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