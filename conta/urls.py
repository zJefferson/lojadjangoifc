# conta/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('minha-conta/', views.minha_conta, name='minha_conta'),
    path('excluir-conta/', views.excluir_conta, name='excluir_conta'),
]