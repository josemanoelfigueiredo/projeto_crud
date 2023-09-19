from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.models import User
def login(request):
    return render(request, 'index.html')

def cadastro_usuario(request):

    email = request.POST.get('email')
    nome = request.POST.get('nome')
    user_name = request.POST.get('user_name')
    senha = request.POST.get('senha')
    confirmar_senha = request.POST.get('confirmar_senha')

    if not Usuario.objects.filter(user__email=email).exists():
        user = User.objects.create_user(user_name, senha, confirmar_senha)
        user.nome
        user.email
        user.save()
        Usuario(user = user).save()
    return render(request, 'auth-register.html')