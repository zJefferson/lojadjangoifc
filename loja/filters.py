# loja/filters.py
import django_filters
from .models import Produto
from django import forms

class ProdutoFilter(django_filters.FilterSet):
    # Filtro para o nome
    nome = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput
    )

    # Filtro para faixa de preço
    preco = django_filters.RangeFilter(
        widget=django_filters.widgets.RangeWidget
    )

    # Filtro para disponibilidade
    disponivel = django_filters.ChoiceFilter(
        choices=((True, 'Disponível'), (False, 'Indisponível')),
        widget=forms.Select,
        empty_label = "Todos"
    )

    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'disponivel']