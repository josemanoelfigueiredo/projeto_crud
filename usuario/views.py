from django.shortcuts import redirect, render
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib import auth

def logout(request):
    auth.logout(request)
    return redirect('login')

def login(request):
    if request.user.is_authenticated:
        return redirect('meus_produtos')
    print('c1')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('c2')
        if Usuario.objects.filter(user__email = email).exists():
            print('c3')
            username = Usuario.objects.get(user__email = email).user.username  #values_list('user__username', flat= True).get()
            user = auth.authenticate(username = username, password = password)
            if user is not None:
                print('c4')
                auth.login(request, user=user)
                return redirect('meus_produtos')
            
    return render(request, 'index.html')


def registrar_usuario(request):
    print('Chegou1')
    if request.method == 'POST':
        nome = request.POST.get('nome')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')
        if not Usuario.objects.filter(user__email = email).exists():    
            if  confirmar_senha == password:
                user = User.objects.create_user(username=username, password=password, email=email)     
                user.save()
                Usuario(user = user, nome_usuario = nome ).save()
                return redirect('login')           
            else:
                print('Não foi possivel criar o usuario')

    return render(request, 'auth-register.html')

def editar_usuario(request):
    usuario = Usuario.objects.get(user = request.user)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

           
        usuario.nome = nome
        usuario.username = username
        usuario.password = password
        usuario.email = email
        usuario.save()
        print('chegou1')
        
    context = {
        'usuario': usuario
    }

    return render(request, 'editar-usuario.html', context)