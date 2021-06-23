from django.db import models
from django import forms
from django.db.models.fields import IntegerField
from usuarios.models import UserProfile
from datetime import datetime

# Create your models here.
SALARIO= (
    ('Até R$ 1.000,00', 'Até R$ 1.000,00'),
    ('De R$ 1.000,00 a 2.000,00', 'De R$ 1.000,00 a 2.000,00'),
    ('De R$ 2.000,00 a 3.000,00', 'De R$ 2.000,00 a 3.000,00'),
    ('Acima de R$ 3.000,00', 'Acima de R$ 3.000,00'),
)

ESCOLARIDADE= (
    ('Ensino fundamental', 'Ensino fundamental'),
    ('Ensino médio', 'Ensino médio'),
    ('Tecnólogo', 'Tecnólogo'),
    ('Ensino Superior', 'Ensino Superior'),
    ('Pós / MBA / Mestrado', 'Pós / MBA / Mestrado'),
    ('Doutorado', 'Doutorado'),
)

class Vaga(models.Model):
    nome_vaga = models.CharField(verbose_name="Vaga", max_length=100)
    salario = models.CharField(verbose_name="Salário", max_length=90, choices=SALARIO)
    descricao = models.TextField(verbose_name="Descrição")
    requisitos = models.TextField(verbose_name="Requisitos")
    escolaridade = models.CharField(verbose_name="Escolaridade", max_length=100, choices=ESCOLARIDADE)
    data_publicacao = models.DateTimeField(verbose_name="Data da publicação")
    empresa = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    candidaturas = models.IntegerField(verbose_name="Candidaturas para essa vaga", default=0)

    def __str__(self):
        return self.nome_vaga
    
    def get_data_publicacao(self):
        return self.data_publicacao.strftime('%d/%m/%Y')


class Candidatura(models.Model):
    candidato = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    pretensao_salarial = models.CharField(verbose_name="Pretensão salarial", max_length=90)
    ultima_escolaridade = models.CharField(verbose_name="Última escolaridade", max_length=100, choices=ESCOLARIDADE)
    experiencia = models.TextField(verbose_name="Experiência")
    pontos = IntegerField()
    data_candidatura = models.DateTimeField(verbose_name="Data da candidatura")


    def get_data_candidatura(self):
        return self.data_candidatura.strftime('%d/%m/%Y')
    

