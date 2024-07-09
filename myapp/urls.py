from django.urls import path
from . import views

urlpatterns = [
   # path('', views.index, name = "index"),
   # path('/segundo', views.segundo, name = 'segundo'),

    #Cursos
    path('/listar_cursos', views.listarCursos,
        name='listar_cursos'),

    path('/incluir_curso', views.incluirCurso, 
        name='incluir_curso'),

]