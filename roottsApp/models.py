from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class Encosta(models.Model):
    nome = models.CharField(max_length=15)
    local = models.CharField(max_length=40)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    declividade = models.DecimalField(max_digits=9, decimal_places=6)
    numeroConstrucoes = models.DecimalField(max_digits=9, decimal_places=6)
    coeficienteUmidade = models.DecimalField(max_digits=5, decimal_places=3)
    proximidadeRedeViarias = models.DecimalField(max_digits=9, decimal_places=6)
    proximidadeCorposLiquidos = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.nome, self.local

class Formulario_denuncia(models.Model):
    nome = models.CharField(max_length = 50)
    data = models.DateField()
    titulo = models.CharField(max_length = 50)
    descricao = models.TextField(max_length=500)


class User(AbstractUser):
    is_engineer = models.BooleanField(default=False)
    is_regularuser = models.BooleanField(default=False)

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