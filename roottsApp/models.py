from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Encosta(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField(max_length=100)
    local = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Formulario_denuncia(models.Model):
    nome = models.CharField(max_length = 20)
    data = models.DateField(blank = True, null = True)
    titulo = models.CharField(max_length = 20)
    descricao = models.TextField(max_length=100)

