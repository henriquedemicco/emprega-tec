from django.test import TestCase
from usuarios.models import UserProfile

from django.urls import reverse


# Teste de Models -------------------------------------------------------------------------------------------

class UserProfileTestCase(TestCase):

    def setUp(self):
        UserProfile.objects.create(
            username='candidato@empregatec.com.br',
            password='candidato123',
            perfil='candidato',
            nome='Pedro'
        )
    
    def test_perfil_retornado(self):
        cdt = UserProfile.objects.get(username='candidato@empregatec.com.br')
        self.assertEquals(cdt.perfil, 'candidato')


