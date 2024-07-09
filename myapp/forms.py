from django.forms import ModelForm 
from django import forms
from .models import Aluno  
from django.forms import ModelForm
from .models import Professor, Curso

class AlunoForm(ModelForm):
   class Meta:
    model = Aluno
    fields = '__all__' 

   data = forms.DateTimeField(
     label = "Data de Nascimento",
     widget=forms.DateTimeInput(
        format='%Y-%m-%d %H:%M:%S',
        attrs={'type': 'date'}
     ),
     input_formats=('%Y-%m-%d %H:%M:%S')
   )  

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
