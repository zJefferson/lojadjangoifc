# loja/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Produto
import django_filters
from .filters import ProdutoFilter
from django.contrib.auth.decorators import login_required
from carrinho.carrinho import Carrinho
# CORREÇÃO: Importando 'messages' de uma forma segura para evitar conflitos
from django.contrib.messages import api as messages_api

# ----- Class-Based View para lista -----
class ListaProdutosView(ListView):
    model = Produto
    template_name = 'lista_produtos.html'
    context_object_name = 'produtos'

# ----- Class-Based View para detalhe -----
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'

# ----- View com filtros -----
def lista_produtos_filtrada(request):
    f = ProdutoFilter(request.GET, queryset=Produto.objects.all())
    return render(request, 'lista_produtos_filtrada.html', {'filter': f})

# ----- Views do Carrinho -----
def adicionar_ao_carrinho(request, produto_id):
    if not request.user.is_authenticated:
        # CORREÇÃO: Usando 'messages_api'
        messages_api.error(request, 'Você precisa estar logado para adicionar produtos ao carrinho.')
        return redirect('login')

    produto = get_object_or_404(Produto, id=produto_id)

    if not produto.disponivel or produto.quantidade <= 0:
        # CORREÇÃO: Usando 'messages_api'
        messages_api.error(request, f'Desculpe, o produto "{produto.nome}" não está mais disponível em estoque.')
        return redirect(request.META.get('HTTP_REFERER', 'lista_produtos'))

    carrinho = Carrinho(request)
    carrinho.adicionar(produto=produto)
    # CORREÇÃO: Usando 'messages_api'
    messages_api.success(request, f'"{produto.nome}" foi adicionado ao seu carrinho!')
    return redirect('ver_carrinho')

@login_required
def remover_do_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho.remover(produto)
    return redirect('ver_carrinho')

@login_required
def ver_carrinho(request):
    carrinho = Carrinho(request)
    return render(request, 'carrinho.html', {'carrinho': carrinho})

@login_required
def checkout(request):
    carrinho = Carrinho(request)
    
    for item in carrinho:
        produto = item['produto']
        quantidade_comprada = item['quantidade']
        
        if produto.quantidade >= quantidade_comprada:
            produto.quantidade -= quantidade_comprada
            produto.save()
        else:
            # CORREÇÃO: Usando 'messages_api'
            messages_api.error(request, f'O produto "{produto.nome}" não tem estoque suficiente.')
            return redirect('ver_carrinho')

    carrinho.limpar()
    return render(request, 'checkout_concluido.html')