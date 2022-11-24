from django.urls import path
from .views import *
from . import views

# path('endereco/', MinhaView.as_view(), name='nome-da-url'),
urlpatterns = [
    path('', InicioView.as_view(), name='home'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('parceria/', ParceriaView.as_view(), name='parceria'),  
    #path('livro/<int:pk>/', LivroInfoView.as_view(), name='info-livro'),
    path('livro/<int:id>/', views.livro_info, name='info-livro'),
    path('autores/', AutoresView.as_view(), name='autores'),
    path('autor/<int:pk>/', AutorInfoView.as_view(), name='info-autor'),
    path('filtroLivro/', LivroFiltroView.as_view(), name='filtro-livro'),
    path('desenvolvedor/', DesenvolvedorView.as_view(), name='desenvolvedor'),
    path('satisfacaoUsuario/', SatisfacaoUserView.as_view(), name='satisfacaoUser'),
    path('satisfacaoBiblioteca/', SatisfacaoBibliView.as_view(), name='satisfacaoBibli'),
    path('faleConosco/', FaleConoscoView.as_view(), name='faleConosco'),
]
