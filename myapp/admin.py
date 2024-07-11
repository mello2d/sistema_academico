from django.contrib import admin
from myapp.models import Aluno, Curso, Professor

# Register your models here.
admin.site.register(Aluno)

admin.site.register(Curso)

admin.site.register(Professor)
