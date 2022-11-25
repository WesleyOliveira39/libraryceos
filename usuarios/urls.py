from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PerfilUpdate
from django.urls import reverse_lazy

urlpatterns = [ 
    path('accounts/login/', auth_views.LoginView.as_view(extra_context={'titulo': 'Autenticação'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('atualizarDados/', PerfilUpdate.as_view(), name='atualizarDados'),
    path('alterar-minha-senha/', auth_views.PasswordChangeView.as_view(
        template_name='usuarios/form.html',
        extra_context={'titulo': 'Alterar senha'},
        success_url=reverse_lazy('home')
    ), name="alterar-senha"),
]

