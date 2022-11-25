from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('cadastrar/autor/', AutorCreate.as_view(), name='cadastrar-autor'),
    path('cadastrar/livro/', LivroCreate.as_view(), name='cadastrar-livro'),
    path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('cadastrar/acervo/', AcervoCreate.as_view(), name='cadastrar-acervo'),

    path('atualizar/autor/<int:pk>/', AutorUpdate.as_view(), name='atualizar-autor'),
    path('atualizar/livro/<int:pk>/', LivroUpdate.as_view(), name='atualizar-livro'),
    path('atualizar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='atualizar-categoria'), 
    path('atualizar/acervo/<int:pk>/', AcervoUpdate.as_view(), name='atualizar-acervo'),

    path('excluir/autor/<int:pk>/', AutorDelete.as_view(), name='excluir-autor'),
    path('excluir/livro/<int:pk>/', LivroDelete.as_view(), name='excluir-livro'),
    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir-categoria'),
    path('excluir/acervo/<int:pk>/', AcervoDelete.as_view(), name='excluir-acervo'),

    path('listar/autores/', AutorList.as_view(), name='listar-autores'),
    path('listar/livros/', LivroList.as_view(), name='listar-livros'),
    path('listar/categorias/', CategoriaList.as_view(), name='listar-categorias'),
    path('listar/acervos/', AcervoList.as_view(), name='listar-acervos'),
    
    path('borrows', views.borrows, name='borrow-page'),
    path('manage_borrow', views.manage_borrow, name='manage-borrow'),
    path('manage_borrow/<int:pk>', views.manage_borrow, name='manage-borrow-pk'),
    path('view_borrow/<int:pk>', views.view_borrow, name='view-borrow-pk'),
    path('save_borrow', views.save_borrow, name='save-borrow'),
    path('delete_borrow/<int:pk>', views.delete_borrow, name='delete-borrow'),
    path('addcomment/<int:id>', views.addcomment, name='addcomment')
]
