from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    # Alunos
    path('listar_aluno', views.listarAluno, name='listar_aluno'),
    path('incluir_aluno', views.incluirAluno, name='incluir_aluno'),
    path('alterar_aluno/<int:id>', views.alterarAluno, name='alterar_aluno'),
    path('excluir_aluno/<int:id>', views.excluirAluno, name='excluir_aluno'),

    # Professores

    path('/listar_professor', views.listarProfessor, name='listar_professor'),
    path('/incluir_professor', views.incluirProfessor, name='incluir_professor'),
    path('/alterar_professor/<int:id>', views.alterarProfessor, name='alterar_professor'),
    path('/excluir_professor/<int:id>', views.excluirProfessor, name='excluir_professor'),

    # Cursos

    path('/listar_cursos', views.listarCursos, name='listar_cursos'),
    path('/incluir_curso', views.incluirCurso, name='incluir_curso'),
    path('/alterar_curso/<int:id>', views.alterarCurso, name='alterar_curso'),
    path('/excluir_curso/<int:id>', views.excluirCurso, name='excluir_curso'),

    # Turmas
    path('/listar_turmas', views.listarTurmas, name='listar_turmas'),
    path('/criar_turma', views.incluirTurma, name='criar_turma'),
   # path('/detalhes_turma/<int:id>', views.detalhesTurma, name='detalhes_turma'),
    path('/editar_turma/<int:id>', views.alterarTurma, name='editar_turma'),
    path('/excluir_turma/<int:id>', views.excluirTurma, name='excluir_turma'),

]
