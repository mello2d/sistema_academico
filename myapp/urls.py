from django.urls import path
from . import views
urlpatterns = [

path ('listar_aluno', views.listarAluno,name='listar_aluno'),
path('incluir_aluno', views.incluirAluno,name='incluir_aluno'),
path('alterar_aluno/<int:id>', views.alterarAluno,name = 'alterar_aluno'),
path ('excluir_aluno/<int:id>', views.excluirAluno, name = 'excluir_aluno'),

]