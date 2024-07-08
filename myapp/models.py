from django.db import models

# Create your models here.
class Curso(models.Models):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

