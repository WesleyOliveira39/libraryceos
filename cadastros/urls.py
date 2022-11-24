from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('cadastrar/autor/', AutorCreate.as_view(), name='cadastrar-autor'),
    path('cadastrar/genero/', GeneroCreate.as_view(), name='cadastrar-genero'),  
    path('cadastrar/livro/', LivroCreate.as_view(), name='cadastrar-livro'),
    path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('cadastrar/acervo/', AcervoCreate.as_view(), name='cadastrar-acervo'),

    path('atualizar/autor/<int:pk>/', AutorUpdate.as_view(), name='atualizar-autor'),
    path('atualizar/genero/<int:pk>/', GeneroUpdate.as_view(), name='atualizar-genero'),  
    path('atualizar/livro/<int:pk>/', LivroUpdate.as_view(), name='atualizar-livro'),
    path('atualizar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='atualizar-categoria'), 
    path('atualizar/acervo/<int:pk>/', AcervoUpdate.as_view(), name='atualizar-acervo'),

    path('excluir/autor/<int:pk>/', AutorDelete.as_view(), name='excluir-autor'),
    path('excluir/genero/<int:pk>/', GeneroDelete.as_view(), name='excluir-genero'),
    path('excluir/livro/<int:pk>/', LivroDelete.as_view(), name='excluir-livro'),
    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir-categoria'),
    path('excluir/acervo/<int:pk>/', AcervoDelete.as_view(), name='excluir-acervo'),

    path('listar/autores/', AutorList.as_view(), name='listar-autores'),
    path('listar/generos/', GeneroList.as_view(), name='listar-generos'),
    path('listar/livros/', LivroList.as_view(), name='listar-livros'),
    path('listar/categorias/', CategoriaList.as_view(), name='listar-categorias'),
    path('listar/acervos/', AcervoList.as_view(), name='listar-acervos'),
    
    path('addcomment/<int:id>', views.addcomment, name='addcomment')
]
