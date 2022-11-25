from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil (models.Model):
    nome = models.CharField(max_length=50, null=True)
    telefone = models.CharField(max_length=11, null=True)
    logradouro = models.CharField(max_length=60, null=True)
    bairro = models.CharField(max_length=60, null=True)
    cidade = models.CharField(max_length=30, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Perfis"

    def __str__(self):
        return str(f"{self.perfil.nome}")

class Instituicao (models.Model):
    STATUS = (
        ('Verificado', 'Verificado'),
        ('Não Verificado', 'Não Verificado'),
    )
    nome_instituicao = models.CharField(max_length=50, verbose_name="Biblioteca")
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=11)
    logradouro = models.CharField(max_length=60)
    bairro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=30)
    status = models.CharField(
        choices=STATUS, max_length=15, default="Não Verificado")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Instituições"

    def __str__(self):
        return str(f"{self.instituicao.nome_instituica}")

    
    
    