from django.shortcuts import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import *
from .forms import ComentarioForm
from django.urls import reverse_lazy #Encaminhar users 
from django.contrib.auth.mixins import LoginRequiredMixin #Controle de Acesso
from braces.views import GroupRequiredMixin #Controle de funcionalidades por grupo de usuários - EX: Bibliotecas <> Administradores
from django.shortcuts import get_object_or_404 #Página de Erro
from django.db.models import Q  #Consultas complexas com objetos Q
from django.contrib.auth.decorators import login_required

#CreateView
#class AutorCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
class AutorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    #group_required = [u"Administrador", u"Biblioteca"]
    model = Autor
    fields = ['nome', 'curriculo_lattes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-autores')
    
    def form_valid(self, form):

        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro - Autores"
        context['descricao'] = "Preenche os seguintes campos:"
        context['botao'] = "Cadastrar"
       
        return context
       
class GeneroCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Genero
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-generos') 
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro - Gêneros"
        context['descricao'] = "Preenche os seguintes campos:"
        context['botao'] = "Cadastrar"
       
        return context   
    
class CategoriaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['genero', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categorias')   
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro - Categorias"
        context['descricao'] = "Preenche os seguintes campos:"
        context['botao'] = "Cadastrar"
       
        return context      
    
class LivroCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Livro
    fields = ['isbn', 'edicao', 'titulo', 'autor', 'ano', 'editora', 'num_page', 'categoria', 'capa', 'resumo']
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
     
class AcervoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Acervo
    fields = ['livro', 'qtdeExemplar']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-acervos')   
    
    def form_valid(self, form): #Sobrescreve o form_valid de CreateView
        
        form.instance.usuario = self.request.user #Criação do objeto e salvamento no BD
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro - Acervo"
        context['descricao'] = "Preenche os seguintes campos:"
        context['botao'] = "Cadastrar"
       
        return context  

#UpdateView
class AutorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Autor
    fields = ['nome', 'curriculo_lattes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-autores')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar - Autores"
        context['descricao'] = "Atualize os campos desejados:"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = "Salvar"
       
        return context  

class GeneroUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Genero
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-generos')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar - Gêneros"
        context['descricao'] = "Atualize os campos desejados:"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = "Salvar"
       
        return context  

class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    fields = ['genero', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-generos')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar - Categorias"
        context['descricao'] = "Atualize os campos desejados:"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = "Salvar"
       
        return context  

class LivroUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Livro
    fields = ['isbn', 'edicao', 'titulo', 'autor', 'ano', 'editora', 'num_page', 'categoria', 'capa', 'resumo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-livros')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar - Livros"
        context['descricao'] = "Atualize os campos desejados:"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = "Salvar"
       
        return context  
    
class AcervoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Acervo
    fields = ['livro', 'qtdeExemplar']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-acervos')
    
    def get_object(self, queryset=None):  #Sobrescreve o get_object de UpdateView 
        self.object = get_object_or_404(Acervo, pk=self.kwargs['pk'], usuario=self.request.user) #kwargs = <int:pk>
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar - Acervo"
        context['descricao'] = "Atualize os campos desejados:"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = "Salvar"
       
        return context  

         
#DeleteView
class AutorDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Autor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-autores')
 
class GeneroDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Genero
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-generos')
    
class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categorias')
        
class LivroDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Livro
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-livros')
    
class AcervoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Acervo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-acervos')
    
    def get_object(self, queryset=None):  #Sobrescreve o get_object de DeleteView 
        self.object = get_object_or_404(Acervo, pk=self.kwargs['pk'], usuario=self.request.user) #kwargs = <int:pk>
        return self.object   
     
#ListView
class AutorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
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
    
    def get_queryset(self): 
        self.object_list = Autor.objects.filter(usuario=self.request.user) 
        return self.object_list
    
class GeneroList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Genero
    template_name = 'cadastros/listas/genero.html'
    paginate_by = 20
    
    def get_queryset(self):
        s = self.request.GET.get('seach')
        if s:
            generos = Genero.objects.filter(descricao__icontains=s)
        else:
            generos = Genero.objects.all()
        return generos
    
class CategoriaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
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
     
class LivroList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
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
    
    def get_queryset(self): 
        self.object_list = Livro.objects.filter(usuario=self.request.user) 
        return self.object_list
     
class AcervoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Acervo
    template_name = 'cadastros/listas/acervo.html'
    paginate_by = 20
  
    def get_queryset(self): #Sobrescreve o get_queryset de ListView
        #self.object_list = Material.objects.all() #Comportamento Padrão > Mostrar todos Users
        self.object_list = Acervo.objects.filter(usuario=self.request.user) 
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
