from django.urls import path
from . import views

urlpatterns = [

    # Cursos

    path('/alterar_curso/<int:id>', views.alterarCurso, name='alterar_curso'),
    path('/excluir_curso/<int;id>', views.excluirCurso, name='excluir_curso'),
]
