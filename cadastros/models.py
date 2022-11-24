from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

class Autor(models.Model):
    nome = models.CharField(max_length=70)
    curriculo_lattes = models.CharField(max_length=16, verbose_name="Currículo Lattes", null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self): #toString in Java
        return "{}".format(self.nome)


class Genero(models.Model):
    descricao = models.CharField(max_length=20, verbose_name="Descrição")

    def __str__(self): 
        return "{}".format(self.descricao)
  
     
class Categoria(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, null=True) 
    descricao = models.CharField(max_length=20, verbose_name="Descrição")

    def __str__(self): 
        return "{}".format(self.descricao)   
    
class Livro(models.Model):
    isbn = models.CharField(max_length=13, null=True, blank=True)
    edicao = models.IntegerField(default=1, verbose_name="Edição", null=True, blank=True)
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT) #Proteger exclusão de tabelas relacionadas
    ano = models.CharField(max_length=4)
    editora = models.CharField(max_length=40, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True)
    num_page = models.IntegerField(verbose_name="Nº Páginas", null=True, blank=True)
    capa = ResizedImageField(
        size=[200,292],
        quality=80,
        default='../static/img/sem_capa.jpg',
        upload_to='img/', 
        null=False, 
        blank=False
    )
    resumo = models.TextField(default="Resumo da Obra")
    consulta = models.PositiveIntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
   
    def __str__(self): 
        return "{} - {}".format(self.titulo, self.autor.nome)
    
class Acervo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    qtdeExemplar = models.IntegerField(verbose_name="Qtde. do Material", default=1)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self): 
        return "{} - {}".format(self.livro.titulo, self.qtdeExemplar)
    
    
class Comentario(models.Model):
    STATUS = (
        ('Lido', 'Lido'),
        ('Não Lido', 'Não Lido'),
    )
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=STATUS, max_length=10, default="Não Lido")

    class Meta:
        verbose_name_plural = "Comentários"

    def __str__(self):
        return self.user.username
