# loja/admin.py
from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'disponivel', 'imagem')
    list_filter = ('disponivel',)
    search_fields = ('nome',)