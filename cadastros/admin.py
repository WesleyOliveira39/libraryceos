from django.contrib import admin
#Impotar Classes
from .models import *

# Classes que podem ser visualizados do painel admin
class AutorAdmin (admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento',
                    'data_falecimento', 'curriculo_lattes', 'rosto',)
    list_editable = ('data_nascimento', 'data_falecimento', 'curriculo_lattes', 'rosto',)
    search_fields = ('nome', 'curriculo_lattes',)
    
class CategoriaAdmin (admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)

class LivroAdmin (admin.ModelAdmin):
    list_display = ('isbn','edicao','titulo','autor','ano','editora','categoria','num_page','capa',)
    list_editable = ('edicao','titulo','autor','ano','editora','categoria','num_page','capa',)
    search_fields = ('isbn','edicao','titulo','autor','ano','editora','categoria','num_page','capa',) 


class ExemplarAdmin (admin.ModelAdmin):
    list_display = ('livro', 'identificador', 'status', 'localizacao',)
    list_editable = ('identificador', 'status', 'localizacao',)
    list_filter = ('status',)


class ComentaAdmin (admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('status',)


admin.site.register(Autor, AutorAdmin)
admin.site.register(Livro,LivroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Exemplar, ExemplarAdmin)
admin.site.register(Borrow)
admin.site.register(Comentario, ComentaAdmin)
