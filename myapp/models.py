from django.db import models

# Create your models here.

# Curso


class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
    valor = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Valor")

    def __str__(self):
        return f"{self.nome} - {self.valor}"

    class Meta:
        ordering = ["nome"]
