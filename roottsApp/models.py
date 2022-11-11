from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class Encosta(models.Model):
    nome = models.CharField(max_length=15)
    local = models.CharField(max_length=40)
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    declividade = models.DecimalField(max_digits=20, decimal_places=10)
    numeroConstrucoes = models.DecimalField(max_digits=20, decimal_places=10)
    coeficienteUmidade = models.DecimalField(max_digits=20, decimal_places=10)
    proximidadeRedeViarias = models.DecimalField(max_digits=20, decimal_places=10)
    proximidadeCorposLiquidos = models.DecimalField(max_digits=20, decimal_places=10)

    PRIORITY_LEVELS = (
        ('Muito Baixo', 'Muito Baixo'),
        ('Baixo', 'Baixo'),
        ('Médio', 'Médio'),
        ('Alto', 'Alto'),
        ('Crítico', 'Crítico'),
    )
    prioridadeEncosta = models.CharField(max_length=30, choices=PRIORITY_LEVELS, default = 'Muito Baixo')

    def __str__(self):
        return self.nome, self.local

class Formulario_denuncia(models.Model):
    nome = models.CharField(max_length = 50)
    endereco = models.TextField(max_length = 100)
    data = models.DateField()
    titulo = models.CharField(max_length = 50)
    descricao = models.TextField(max_length=500)
    aprovado = models.BooleanField('aprovado', default=False)


    def __str__(self):
        return self.nome

class User(AbstractUser):
    is_engineer = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class EngineerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    crea = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class RegularUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome
