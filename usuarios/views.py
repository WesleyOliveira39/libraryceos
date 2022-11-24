from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Perfil


# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    #success_url = reverse_lazy('login')
    success_url = reverse_lazy('index') 
   
    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="Biblioteca")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()
        
        Perfil.objects.create(usuario=self.object) #Cria-se um perfil, após criação do user
        return url  
   
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registros - Usuários"
        context['botao'] = "Registrar"

        return context

class PerfilUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Perfil
    fields = ["nome_instituicao", "cnpj", "telefone", "logradouro", "bairro", "cidade"]
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Dados da Biblioteca"
        context["botao"] = "Atualizar"

        return context



    
    
   