from django.forms import ModelForm 
from .models import Aluno  
from django.forms import ModelForm
from .models import Professor, Curso

class AlunoForm(ModelForm):
   class Meta:
    model = Aluno
    fields = '__all__' 


class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
