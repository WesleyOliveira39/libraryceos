from django.db import models
from django.contrib.auth.models import User
from django.forms import DateInput, RadioSelect, TextInput, Textarea
from django_resized import ResizedImageField
from django.utils import timezone
from usuarios.models import Perfil


class Autor(models.Model):
    nome = models.CharField(max_length=70)
    data_nascimento = models.DateField()
    data_falecimento = models.DateField(null=True, blank=True)
    local_nascimento = models.CharField(max_length=100)
    biografia = models.TextField(default="Biografia do Autor")
    rosto = ResizedImageField(
        size=[200, 292],
        quality=80,
        default='../static/assets/img/sem_rosto.jpg',
        upload_to='img/',
        null=False,
        blank=False
    )
    curriculo_lattes = models.CharField(
        max_length=16, verbose_name="Currículo Lattes", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return "{}".format(self.nome)


class Categoria(models.Model):
    descricao = models.CharField(max_length=40, verbose_name="Descrição")

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return "{}".format(self.descricao)


class Livro(models.Model):
    isbn = models.CharField(max_length=13)
    edicao = models.IntegerField(
        default=1, verbose_name="Edição", null=True, blank=True)
    titulo = models.CharField(max_length=100)
    # Proteger exclusão de tabelas relacionadas
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    ano = models.DateField()
    editora = models.CharField(max_length=40, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    num_page = models.IntegerField(
        verbose_name="Nº Páginas", null=True, blank=True)
    capa = ResizedImageField(
        size=[200, 292],
        quality=80,
        default='../static/assets/img/sem_capa.jpg',
        upload_to='img/',
        null=False,
        blank=False
    )
    resumo = models.TextField(default="Resumo da Obra")
    consulta = models.PositiveIntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Livros"

    def __str__(self):
        return "{} - {}".format(self.titulo, self.autor.nome)


class Exemplar(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    identificador = models.CharField(max_length=5)
    status = models.CharField(max_length=2, choices=(
        ('1', 'Disponível'), ('2', 'Indisponível')), default=1)
    localizacao = models.CharField(
        max_length=15, verbose_name="Localização", null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Exemplares"

    def __str__(self):
        return "{} - {}".format(self.livro.titulo, self.identificador)


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


class Borrow(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuário")
    book = models.ForeignKey(Exemplar, on_delete=models.CASCADE, verbose_name="Exemplar")
    borrowing_date = models.DateField(verbose_name="Data de retirada")
    return_date = models.DateField(verbose_name="Data de devolução")
    status = models.CharField(max_length=2, choices=(
        ('1', 'Pendente'), ('2', 'OK')), default=1)
    date_added = models.DateTimeField(
        default=timezone.now, verbose_name="Horário de Criação")
    date_created = models.DateTimeField(
        auto_now=True, verbose_name="Data de criação")

    class Meta:
        verbose_name_plural = "Empréstimos"

    def __str__(self):
        return str(f"{self.book.identificador}")
