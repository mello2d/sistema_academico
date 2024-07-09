from django.urls import path
from . import views

<<<<<<< HEAD
=======
from django.urls import path
from . import views

>>>>>>> 4cc940341912d4dde67eea9ca79eda86f139860d
urlpatterns = [
    path('', views.index, name="index"),

    # professores

    path('/listar_professor', views.listarProfessor, name='listar_professor'),
    path('/incluir_professor', views.incluirProfessor, name='incluir_professor'),
    path('/alterar_professor', views.alterarProfessor, name='alterar_professor'),
    path('/excluir_professor', views.excluirProfessor, name='excluir_professor'),

    # Cursos
<<<<<<< HEAD
    path('/alterar_curso/<int:id>', views.alterarCurso, name='alterar_curso'),
    path('/excluir_curso/<int:id>', views.excluirCurso, name='excluir_curso'),

    path('/listar_cursos', views.listarCursos,
        name='listar_cursos'),

    path('/incluir_curso', views.incluirCurso, 
        name='incluir_curso'),

=======

    path('/alterar_curso/<int:id>', views.alterarCurso, name='alterar_curso'),
    path('/excluir_curso/<int:id>', views.excluirCurso, name='excluir_curso'),

>>>>>>> 4cc940341912d4dde67eea9ca79eda86f139860d
]
