from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('/segundo', views.segundo, name = 'segundo'),

    #Cursos
    path('/listar_curso', views.listarCursos,
        name='listar_curso'),

    path('/incluir_curso', views.incluirCurso, 
        name='incluir_curso'),

]