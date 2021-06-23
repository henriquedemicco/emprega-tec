from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


# Create your models here.

class UserProfile(AbstractUser):
    empresa = models.CharField(max_length=100) 
    perfil = models.CharField(max_length=100)
    foto = models.ImageField(verbose_name='Foto', upload_to='media', blank=True)



