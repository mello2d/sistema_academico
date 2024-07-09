from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('listar_aluno', views.listarAluno, name='listar_aluno'),
    path('incluir_aluno', views.incluirAluno, name='incluir_aluno'),
    path('alterar_aluno/<int:id>', views.alterarAluno, name='alterar_aluno'),
    path('excluir_aluno/<int:id>', views.excluirAluno, name='excluir_aluno'),

    # professores

    path('/listar_professor', views.listarProfessor, name='listar_professor'),
    path('/incluir_professor', views.incluirProfessor, name='incluir_professor'),
    path('/alterar_professor/<int:id>', views.alterarProfessor, name='alterar_professor'),
    path('/excluir_professor/<int:id>', views.excluirProfessor, name='excluir_professor'),

    # Cursos


    path('/listar_cursos', views.listarCursos, name='listar_cursos'),
    path('/incluir_curso', views.incluirCurso, name='incluir_curso'),
    path('/alterar_curso/<int:id>', views.alterarCurso, name='alterar_curso'),
    path('/excluir_curso/<int:id>', views.excluirCurso, name='excluir_curso'),
]
