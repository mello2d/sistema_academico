from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)      
    def __str__(self):
        return f'{self.nome} - {self.telefone} - {self.email}' - {self.data}

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)  
    def __str__(self):
        return f'{self.nome} - {self.email} - {self.telefone}'

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
    valor = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Valor")

    def __str__(self):
        return f"{self.nome} - {self.valor}"

    class Meta:
        ordering = ["nome"]


class Turma(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    data_inicio = models.DateField()
    data_termino = models.DateField()

    def __str__(self):
        return f'Turma de {self.curso}'


