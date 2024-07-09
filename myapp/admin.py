from django.contrib import admin
from myapp.models import Professor

from myapp.models import Curso

# Register your models here.
admin.site.register(Curso)
admin.site.register(Professor)
