from django.test import TestCase
from ..models import *


class CreateEncostaTest(TestCase):
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

        def test_encosta_creation(self):
                self.assertTrue(isinstance(self.encosta, Encosta))
                self.assertEqual(self.encosta.__str__(), (self.encosta.nome, self.encosta.local))
                

class CreateDenunciaTest(TestCase):
        def setUp(self):
                self.denuncia = Formulario_denuncia.objects.create(
                nome='DenunciaTeste',
                data='2019-05-01',
                titulo='Titulo1',
                descricao='Descricao1')
                self.denuncia.save()

        def test_denuncia_creation(self):
                self.assertTrue(isinstance(self.denuncia, Formulario_denuncia))
                self.assertEqual(self.denuncia.__str__(), self.denuncia.nome)


class UserTestCase(TestCase):
        def setUp(self):
                self.user = User.objects.create_user(username='testuser', password='12345')
                self.user.save()
        
        def test_user(self):
                self.assertEqual(self.user.username, 'testuser')
                self.assertNotEqual(self.user.password, '12345')

