# loja/urls.py
from django.urls import path
from .views import (
    ListaProdutosView, 
    ProdutoDetailView, 
    lista_produtos_filtrada,
    adicionar_ao_carrinho,  # Certifique-se que esta linha foi adicionada
    remover_do_carrinho,    # Certifique-se que esta linha foi adicionada
    ver_carrinho,
    checkout,               # Certifique-se que esta linha foi adicionada
)

urlpatterns = [
    path('', ListaProdutosView.as_view(), name='lista_produtos'),
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('filtrados/', lista_produtos_filtrada, name='produtos_filtrados'),
    path('adicionar/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:produto_id>/', remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/', ver_carrinho, name='ver_carrinho'),
    path('carrinho/checkout/', checkout, name='checkout'), 
]
