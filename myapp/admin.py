from django.contrib import admin
from myapp.models import Aluno
from myapp.models import Professor

from myapp.models import Curso

admin.site.register(Aluno)
# Register your models here.
admin.site.register(Curso)

# Register your models here.

admin.site.register(Professor)
