from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil (models.Model):
    nome_instituicao = models.CharField(max_length=50, null=True)
    cnpj = models.CharField(max_length=14, null=True)
    telefone = models.CharField(max_length=11, null=True)
    logradouro = models.CharField(max_length=60, null=True)
    bairro = models.CharField(max_length=60, null=True)
    cidade = models.CharField(max_length=30, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE) #Relação 1 para 1 - User e Perfil
    
    
    