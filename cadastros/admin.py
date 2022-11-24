from django.contrib import admin
#Impotar Classes
from .models import *

# Classes que podem ser visualizados do painel admin
class AutorAdmin (admin.ModelAdmin):
    list_display = ('nome', 'curriculo_lattes',)
    search_fields = ('nome', 'curriculo_lattes',)
    
class AcervoAdmin (admin.ModelAdmin):
    list_display = ('livro', 'qtdeExemplar', 'usuario',)
    search_fields = ('livro', 'qtdeExemplar', 'usuario',) 

class GeneroAdmin (admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    
class LivroAdmin (admin.ModelAdmin):
    list_display = ('isbn','edicao','titulo','autor','ano','editora','categoria','num_page','capa',)
    list_editable = ('edicao','titulo','autor','ano','editora','categoria','num_page','capa',)
    search_fields = ('isbn','edicao','titulo','autor','ano','editora','categoria','num_page','capa',) 

class CategoriaAdmin (admin.ModelAdmin):
    list_display = ('genero','descricao',)
    list_editable = ('descricao',)
    search_fields = ('genero','descricao',) 


class ComentaAdmin (admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('status',)


admin.site.register(Autor, AutorAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Livro,LivroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Acervo, AcervoAdmin)
admin.site.register(Comentario, ComentaAdmin)
