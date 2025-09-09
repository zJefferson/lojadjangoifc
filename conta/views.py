# conta/views.py
from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

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

@login_required
def minha_conta(request):
    return render(request, 'minha_conta.html')

@login_required
def excluir_conta(request):
    if request.method == 'POST':
        # Pega o usuário logado
        user = request.user
        # Desloga o usuário antes de deletar
        logout(request)
        # Deleta o usuário do banco de dados
        user.delete()
        # Envia uma mensagem de sucesso
        messages.success(request, 'Sua conta foi excluída com sucesso.')
        # Redireciona para a página inicial
        return redirect('lista_produtos')
    
    # Se não for POST, apenas mostra a página de confirmação
    return render(request, 'excluir_conta_confirm.html')