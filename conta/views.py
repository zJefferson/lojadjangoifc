# conta/views.py
from django.shortcuts import render, redirect
from .forms import RegistroForm

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Cria um novo usuário mas não salva ainda no banco de dados
            novo_usuario = form.save(commit=False)
            # Define a senha escolhida
            novo_usuario.set_password(form.cleaned_data['password'])
            # Salva o usuário no banco de dados
            novo_usuario.save()
            return render(request, 'registro_concluido.html', {'novo_usuario': novo_usuario})
    else:
        form = RegistroForm()
    
    return render(request, 'registrar.html', {'form': form})