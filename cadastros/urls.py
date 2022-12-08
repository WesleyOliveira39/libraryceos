from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('cadastrar/autor/', AutorCreate.as_view(), name='cadastrar-autor'),
    path('cadastrar/livro/', LivroCreate.as_view(), name='cadastrar-livro'),
    path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('cadastrar/exemplar/', ExemplarCreate.as_view(), name='cadastrar-exemplar'),
    path('cadastrar/emprestimo/', EmprestimoCreate.as_view(), name='cadastrar-emprestimo'),

    path('atualizar/autor/<int:pk>/', AutorUpdate.as_view(), name='atualizar-autor'),
    path('atualizar/livro/<int:pk>/', LivroUpdate.as_view(), name='atualizar-livro'),
    path('atualizar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='atualizar-categoria'), 
    path('atualizar/exemplar/<int:pk>/', ExemplarUpdate.as_view(), name='atualizar-exemplar'),
    path('atualizar/emprestimo/<int:pk>/', EmprestimoUpdate.as_view(), name='atualizar-emprestimo'),

    path('excluir/autor/<int:pk>/', AutorDelete.as_view(), name='excluir-autor'),
    path('excluir/livro/<int:pk>/', LivroDelete.as_view(), name='excluir-livro'),
    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir-categoria'),
    path('excluir/exemplar/<int:pk>/', ExemplarDelete.as_view(), name='excluir-exemplar'),
    path('excluir/emprestimo/<int:pk>/', EmprestimoDelete.as_view(), name='excluir-emprestimo'),

    path('listar/autores/', AutorList.as_view(), name='listar-autores'),
    path('listar/livros/', LivroList.as_view(), name='listar-livros'),
    path('listar/categorias/', CategoriaList.as_view(), name='listar-categorias'),
    path('listar/exemplares/', ExemplarList.as_view(), name='listar-exemplares'),
    path('listar/emprestimos/', EmprestimoList.as_view(), name='listar-emprestimos'),
       
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    
    path('borrows', views.borrows, name='borrow-page'),
    path('manage_borrow', views.manage_borrow, name='manage-borrow'),
    path('manage_borrow/<int:pk>', views.manage_borrow, name='manage-borrow-pk'),
    path('view_borrow/<int:pk>', views.view_borrow, name='view-borrow-pk'),
    path('save_borrow', views.save_borrow, name='save-borrow'),
]
