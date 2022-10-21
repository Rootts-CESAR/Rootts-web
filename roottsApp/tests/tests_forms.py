from django.test import TestCase
from django.urls import reverse


from ..forms import *



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
    def setup(self):
        self.user = User.objects.create_user(
            username='user1',
            password='12345'
        )
        self.user.save()
        self.client.login(username='user1', password='12345')
        self.denuncia = Formulario_denuncia.objects.create(
            nome='DenunciaTeste',
            data='2019-05-01',
            titulo='Titulo1',
            descricao='Descricao1'
        )
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


class EngiennerUseCreationFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user1',
            password='12345'
        )
        self.user.save()
        self.engenheiro = EngineerUser.objects.create(
            user=self.user,
            nome='Engenheiro1',
            email='EngenheiroTeste@gmail.com',
            crea='123123',
        )
        self.engenheiro.save()

    def test_engenheiro_form(self):
        data = {
            'user': self.user,
            'username': 'Engenheiro1',
            'nome': 'Engenheiro1',
            'email': 'Engenheiroteste@gmail.com',
            'crea': '123123',
            'password1': '123456Ab@',
            'password2': '123456Ab@'
        }
        form = EngineerUserCreationForm(data=data)
        self.assertTrue(form.is_valid())


class RegularUserCreationFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user1',
            password='12345'
        )
        self.user.save()
        self.regularUser = RegularUser.objects.create(
            user=self.user,
            nome='UsuarioComuns',
            email='regularUser@gmail.com',
        )
        self.regularUser.save()

    def test_engenheiro_form(self):
        data = {
            'user': self.user,
            'username': 'UsuarioComum',
            'nome': 'UsuarioComuns',
            'email': 'regularUser@gmail.com',
            'password1': '123456Ab@',
            'password2': '123456Ab@'
        }
        form = RegularUserCreationForm(data=data)
        self.assertTrue(form.is_valid())