from django.contrib import admin
from .models import Municipio, Escritor, Livro, Membro

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id')

@admin.register(Escritor)
class EscritorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'municipio', 'descricao')

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'link', 'autor')

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'funcao', 'lattes')