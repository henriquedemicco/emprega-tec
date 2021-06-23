from django.test import TestCase

from django.urls import reverse

# Create your tests here.

# Teste de Views -------------------------------------------------------------------------------------------

class PrincipalViewTest(TestCase):

    def test_status_code_200(self):
        response = self.client.get(reverse('principal'))
        self.assertEquals(response.status_code, 200)
    
    def test_template_utilizado(self):
        response = self.client.get(reverse('principal'))
        self.assertTemplateUsed(response, 'index.html')