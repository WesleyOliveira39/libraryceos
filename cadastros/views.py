import json
from django.shortcuts import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import *
from .forms import ComentarioForm
from django.urls import reverse_lazy  # Encaminhar users
from django.contrib.auth.mixins import LoginRequiredMixin  # Controle de Acesso
# Controle de funcionalidades por grupo de usuários - EX: Bibliotecas <> Administradores
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404  # Página de Erro
from django.db.models import Q  # Consultas complexas com objetos Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from cadastros import forms, models


class AutorCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Autor
    fields = ['nome', 'data_nascimento', 'data_falecimento',
              'local_nascimento', 'biografia', 'rosto', 'curriculo_lattes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-autores')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro - Autores"
        context['descricao'] = "Preenche os seguintes campos:"
        context['botao'] = "Cadastrar"

        return context


class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Categoria
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categorias')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro - Categorias"
        context['descricao'] = "Preenche os seguintes campos:"
        context['botao'] = "Cadastrar"

        return context


class LivroCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Livro
    fields = ['isbn', 'edicao', 'titulo', 'autor', 'ano',
              'editora', 'num_page', 'categoria', 'capa', 'resumo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-livros')

    def form_valid(self, form):

        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro - Livros"
        context['descricao'] = "Preenche os seguintes campos:"
        context['botao'] = "Cadastrar"

        return context


class ExemplarCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Exemplar
    fields = ['livro', 'identificador', 'status', 'localizacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-exemplares')

    def form_valid(self, form):  # Sobrescreve o form_valid de CreateView

        # Criação do objeto e salvamento no BD
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro - Acervo"
        context['descricao'] = "Preenche os seguintes campos:"
        context['botao'] = "Cadastrar"

        return context


class EmprestimoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Borrow
    fields = ['student', 'book', 'borrowing_date', 'return_date']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-emprestimos')

    def form_valid(self, form):  # Sobrescreve o form_valid de CreateView

        # Criação do objeto e salvamento no BD
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Empréstimo"
        context['descricao'] = "Preenche os seguintes campos:"
        context['botao'] = "Cadastrar"

        return context



#UpdateView
class AutorUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Autor
    fields = ['nome', 'data_nascimento', 'data_falecimento',
              'local_nascimento', 'biografia', 'rosto', 'curriculo_lattes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-autores')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar - Autores"
        context['descricao'] = "Atualize os campos desejados:"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = "Salvar"

        return context


class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Categoria
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-generos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar - Categorias"
        context['descricao'] = "Atualize os campos desejados:"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = "Salvar"

        return context


class LivroUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Livro
    fields = ['isbn', 'edicao', 'titulo', 'autor', 'ano',
              'editora', 'num_page', 'categoria', 'capa', 'resumo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-livros')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar - Livros"
        context['descricao'] = "Atualize os campos desejados:"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = "Salvar"

        return context


class ExemplarUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Exemplar
    fields = ['livro', 'identificador', 'status', 'localizacao', ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-exemplares')

    def get_object(self, queryset=None):  # Sobrescreve o get_object de UpdateView
        self.object = get_object_or_404(
            Exemplar, pk=self.kwargs['pk'], usuario=self.request.user)  # kwargs = <int:pk>
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar - Acervo"
        context['descricao'] = "Atualize os campos desejados:"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = "Salvar"

        return context

class EmprestimoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Borrow
    fields = ['book', 'borrowing_date', 'return_date']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-emprestimos')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar - Empréstimo"
        context['descricao'] = "Atualize os campos desejados:"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = "Salvar"

        return context

#DeleteView
class AutorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    model = Autor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-autores')


class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categorias')


class LivroDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    model = Livro
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-livros')


class ExemplarDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Exemplar
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-exemplares')

    def get_object(self, queryset=None):  # Sobrescreve o get_object de DeleteView
        self.object = get_object_or_404(
            Exemplar, pk=self.kwargs['pk'], usuario=self.request.user)  # kwargs = <int:pk>
        return self.object


class EmprestimoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Borrow
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-emprestimos')


#ListView
class AutorList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Autor
    template_name = 'cadastros/listas/autor.html'
    paginate_by = 20

    def get_queryset(self):
        s = self.request.GET.get('seach')
        if s:
            autores = Autor.objects.filter(nome__icontains=s)
        else:
            autores = Autor.objects.all()
        return autores


class CategoriaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'
    paginate_by = 20

    def get_queryset(self):
        s = self.request.GET.get('seach')
        if s:
            categorias = Categoria.objects.filter(descricao__icontains=s)
        else:
            categorias = Categoria.objects.all()
        return categorias


class LivroList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Livro
    template_name = 'cadastros/listas/livro.html'
    paginate_by = 20

    def get_queryset(self):
        s = self.request.GET.get('seach')
        if s:
            multiple_q = Q(Q(titulo__icontains=s) |
                           Q(autor__nome__icontains=s) | Q(editora__icontains=s))
            livros = Livro.objects.filter(multiple_q)
        else:
            livros = Livro.objects.all()
        return livros

class ExemplarList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Exemplar
    template_name = 'cadastros/listas/exemplar.html'
    paginate_by = 20

    def get_queryset(self):
        s = self.request.GET.get('seach')
        if s:
            multiple_q = Q(Q(livro__titulo__icontains=s) |
                           Q(livro__isbn__icontains=s) | Q(identificador__icontains=s))
            exemplares = Exemplar.objects.filter(multiple_q)
        else:
            exemplares = Exemplar.objects.all()
        return exemplares

    def get_queryset(self):  # Sobrescreve o get_queryset de ListView
        #self.object_list = Material.objects.all() #Comportamento Padrão > Mostrar todos Users
        self.object_list = Exemplar.objects.filter(usuario=self.request.user)
        return self.object_list
    

class EmprestimoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Bibliotecas"]
    model = Borrow
    template_name = 'cadastros/listas/emprestimo.html'
    paginate_by = 20

    def get_queryset(self):
        s = self.request.GET.get('seach')
        if s:
            multiple_q = Q(Q(livro__titulo__icontains=s) | Q(status__icontains=s) |
                           Q(livro__isbn__icontains=s) | Q(user__perfil__nome__icontains=s))
            emprestimos = Borrow.objects.filter(multiple_q)
        else:
            emprestimos = Borrow.objects.all()
        return emprestimos
    
    def get_queryset(self):  # Sobrescreve o get_queryset de ListView
        #self.object_list = Material.objects.all() #Comportamento Padrão > Mostrar todos Users
        self.object_list = Borrow.objects.filter(book__usuario=self.request.user)
        return self.object_list

@login_required
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            data = Comentario()
            data.comentario = form.cleaned_data['comentario']
            data.user = request.user
            data.livro_id = id
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


def context_data(request):
    fullpath = request.get_full_path()
    abs_uri = request.build_absolute_uri()
    abs_uri = abs_uri.split(fullpath)[0]
    context = {
        'system_host': abs_uri,
        'page_name': '',
        'page_title': '',
        'system_name': 'Library Managament System',
        'topbar': True,
        'footer': True,
    }

    return context


@login_required
def borrows(request):
    context = context_data(request)
    context['page'] = 'borrow'
    context['page_title'] = "Borrowing Transaction List"
    context['borrows'] = models.Borrow.objects.order_by('status').all()
    return render(request, 'borrows.html', context)


@login_required
def save_borrow(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        post = request.POST
        if not post['id'] == '':
            borrow = models.Borrow.objects.get(id=post['id'])
            form = forms.SaveBorrow(request.POST, instance=borrow)
        else:
            form = forms.SaveBorrow(request.POST)

        if form.is_valid():
            form.save()
            if post['id'] == '':
                messages.success(
                    request, "Borrowing Transaction has been saved successfully.")
            else:
                messages.success(
                    request, "Borrowing Transaction has been updated successfully.")
            resp['status'] = 'success'
        else:
            for field in form:
                for error in field.errors:
                    if not resp['msg'] == '':
                        resp['msg'] += str('<br/>')
                    resp['msg'] += str(f'[{field.name}] {error}')
    else:
        resp['msg'] = "There's no data sent on the request"

    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def view_borrow(request, pk=None):
    context = context_data(request)
    context['page'] = 'view_borrow'
    context['page_title'] = 'View Transaction Details'
    if pk is None:
        context['borrow'] = {}
    else:
        context['borrow'] = models.Borrow.objects.get(id=pk)

    return render(request, 'view_borrow.html', context)


@login_required
def manage_borrow(request, pk=None):
    context = context_data(request)
    context['page'] = 'manage_borrow'
    context['page_title'] = 'Manage Transaction Details'
    if pk is None:
        context['borrow'] = {}
    else:
        context['borrow'] = models.Borrow.objects.get(id=pk)
    #livro = Livro.objects.get(pk=id)
    #context['students'] = models.User.objects.filter(username=request.user)
    #multiple_q = Q(Q(status__icontains=1) | Q(livro__id__icontains=livro))
    context['books'] = models.Exemplar.objects.all()
    return render(request, 'manage_borrow.html', context)

@login_required
def delete_borrow(request, pk=None):
    resp = {'status': 'failed', 'msg': ''}
    if pk is None:
        resp['msg'] = 'Transaction ID is invalid'
    else:
        try:
            models.Borrow.objects.filter(pk=pk).delete()
            messages.success(
                request, "Transaction has been deleted successfully.")
            resp['status'] = 'success'
        except:
            resp['msg'] = "Deleting Transaction Failed"

    return HttpResponse(json.dumps(resp), content_type="application/json")
