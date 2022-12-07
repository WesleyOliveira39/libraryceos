from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from cadastros.models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
#from .forms import ComentarioForm



# Create your views here.

#class ModeloView(TemplateView): #Herança - Extends em Java
#    template_name = "core/modelo.html"
 
class InicioView(ListView):
    model = Livro
    template_name = "core/home.html"
    paginate_by = 10

    def get_queryset(self):
        s = self.request.GET.get('seach')
        if s:
            multiple_q = Q(Q(titulo__icontains=s) |
                           Q(autor__nome__icontains=s) | Q(editora__icontains=s) | Q(categoria__descricao__icontains=s))
            livros = Livro.objects.filter(multiple_q)
        else:
            livros = Livro.objects.all()
        return livros

    #Ordenar com base no último cadastro
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['livro_list'] = Livro.objects.all().order_by("-id")
        return context


def livro_info(request, id):
    livro = Livro.objects.get(pk=id)
    livro.consulta += 1
    livro.save()
    comentarios = Comentario.objects.filter(livro_id=id, status='Não Lido')
    total = 0
    for i in comentarios:
        total = total + 1

    context = {
        'livro': livro,
        'comentarios': comentarios,
        'total': total}

    return render(request, 'core/info-livro.html', context)

#class LivroInfoView (DetailView):
#    model = Livro
#    template_name = "core/info-livro.html"
#    pk_fiel = "pk"


class LivroFiltroView (ListView):
    #model = Acervo
    template_name = "core/filtro-livro.html"
    #paginate_by = 10


class AutoresView(ListView):
    model = Autor
    template_name = 'core/autores.html'
    paginate_by = 20

    def get_queryset(self):
        s = self.request.GET.get('seach')
        if s:
            autores = Autor.objects.filter(nome__icontains=s)
        else:
            autores = Autor.objects.all()
        return autores

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autor_random'] = Autor.objects.all().order_by('?')[:5]
        return context


class AutorInfoView (DetailView):
    model = Autor
    template_name = "core/info-autor.html"
    pk_fiel = "pk"


class SobreView(TemplateView):
    template_name = "core/sobre.html"


class ParceriaView(TemplateView):
    template_name = "core/parceria.html"


class DesenvolvedorView(TemplateView):
    template_name = "core/desenvolvedor.html"


class SatisfacaoUserView(TemplateView):
    template_name = "core/satisfacaoUser.html"


class SatisfacaoBibliView(TemplateView):
    template_name = "core/satisfacaoBibli.html"


class FaleConoscoView(TemplateView):
    template_name = "core/faleConosco.html"






