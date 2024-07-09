
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    # professores

    path('/listar_professor', views.listarProfessor, name='listar_professor'),
    path('/incluir_professor', views.incluirProfessor, name='incluir_professor'),
    path('/alterar_professor', views.alterarProfessor, name='alterar_professor'),
    path('/excluir_professor', views.excluirProfessor, name='excluir_professor'),

    # Cursos

    path('/alterar_curso/<int:id>', views.alterarCurso, name='alterar_curso'),
    path('/excluir_curso/<int:id>', views.excluirCurso, name='excluir_curso'),

]
