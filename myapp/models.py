from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)      
    def __str__(self):
        return f'{self.nome} - {self.telefone} - {self.email}' - {self.data}
