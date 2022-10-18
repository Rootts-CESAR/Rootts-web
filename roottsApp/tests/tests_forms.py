from django.test import TestCase
from django.urls import reverse

from ..forms import *

# Create your tests here.

class EncostaFormTest(TestCase):
    def setUp(self):
        self.encosta = Encosta.objects.create(
            nome='Encosta1',
            local='Local1',
            latitude=1,
            longitude=1,                    
            declividade=1,
            numeroConstrucoes=1,
            coeficienteUmidade=1,
            proximidadeRedeViarias=1,
            proximidadeCorposLiquidos=1)
        self.encosta.save()


    def test_encosta_form(self):
        data = {
            'nome': 'Encosta1',
            'local': 'Local1',
            'latitude': 1,
            'longitude': 1,                    
            'declividade': 1,
            'numeroConstrucoes': 1,
            'coeficienteUmidade': 1,
            'proximidadeRedeViarias': 1,
            'proximidadeCorposLiquidos': 1
        }
        form = EncostaForm(data=data)
        self.assertTrue(form.is_valid())


class EncostaFormUpdateTest(TestCase):
    def setUp(self):
        self.encosta = Encosta.objects.create(
            nome='Encosta1',
            local='Local1',
            latitude=1,
            longitude=1,                    
            declividade=1,
            numeroConstrucoes=1,
            coeficienteUmidade=1,
            proximidadeRedeViarias=1,
            proximidadeCorposLiquidos=1)
        self.encosta.save()


    def test_encosta_form(self):
        data = {
            'nome': 'Encosta1',
            'local': 'Local1',
            'latitude': 1,
            'longitude': 1,                    
            'declividade': 1,
            'numeroConstrucoes': 1,
            'coeficienteUmidade': 1,
            'proximidadeRedeViarias': 1,
            'proximidadeCorposLiquidos': 1
        }
        form = EncostaFormUpdate(data=data)
        self.assertTrue(form.is_valid())


class DenunciaFormTest(TestCase):
    def setUp(self):
        self.denuncia = Formulario_denuncia.objects.create(
            nome='DenunciaTeste',
            data='2019-05-01',
            titulo='Titulo1',
            descricao='Descricao1')
        self.denuncia.save()


    def test_denuncia_form(self):
        data = {
            'nome': 'DenunciaTeste',
            'data': '2019-05-01',
            'titulo': 'Titulo1',
            'descricao': 'Descricao1'
        }
        form = denunciaForm(data=data)
        self.assertTrue(form.is_valid())


class RegularUserCreationFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.save()


    def test_user_form(self):
        data = {
            'username': 'TestRegularUser',
            'password': '12345',
            'password2': '12345'
        }
        form = RegularUserCreationForm(data=data)
        self.assertTrue(form.is_regular_user())
        self.assertTrue(form.is_valid())


class EngineerUserCreationFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.save()


    def test_user_form(self):
        data = {
            'username': 'TestEngineerUser',
            'password': '12345',
            'password2': '12345'
        }

        form = EngineerUserCreationForm(data=data)
        self.assertTrue(form.is_engineer_user())
        self.assertTrue(form.is_valid())