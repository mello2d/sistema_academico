from django.forms import ModelForm 
from django import forms
from .models import Aluno, Professor, Curso, Turma

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

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'
    data_inicio = forms.DateTimeField(
     label = "Data de início",
     widget=forms.DateTimeInput(
        format='%Y-%m-%d %H:%M:%S',
        attrs={'type': 'date'}
     ),
     input_formats=('%Y-%m-%d %H:%M:%S')
   )
    data_termino = forms.DateTimeField(
     label = "Data de Termino",
     widget=forms.DateTimeInput(
        format='%Y-%m-%d %H:%M:%S',
        attrs={'type': 'date'}
     ),
     input_formats=('%Y-%m-%d %H:%M:%S')
   )  
