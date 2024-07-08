from django.forms import ModelForm

from myapp.models import Curso


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
