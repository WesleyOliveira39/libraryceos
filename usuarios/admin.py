from django.contrib import admin
from .models import *

class InstituicaoAdmin (admin.ModelAdmin):
    list_display = ('nome_instituicao', 'cnpj', 'telefone', 'logradouro', 'bairro', 'cidade',)
    list_editable = ('cnpj', 'telefone', 'logradouro', 'bairro', 'cidade',)
    list_filter = ('nome_instituicao',)


class PerfilAdmin (admin.ModelAdmin):
    list_display = ('nome', 'telefone','logradouro', 'bairro', 'cidade',)
    list_editable = ('telefone', 'logradouro', 'bairro', 'cidade',)
    list_filter = ('nome',)


# Register your models here.
admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(Perfil, PerfilAdmin)
