from django.shortcuts import render
from .models import Produto
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'index.html')

def meus_produtos(request):
    produtos = Produto.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(produtos,6)
    try: 
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)


    context = {
        'produtos': result,

    }



    return render(request, 'meus-produtos.html', context)



def dashboard(request):
    return render(request, 'dashboard.html')

def editar_produto(request, id_produto):
    produto = Produto.objects.get(id_produto=id_produto)

    if request.method == 'POST':
        produto = Produto()
        produto.nome = request.POST.get('nome')
        produto.email = request.POST.get('email')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.foto_produto = request.FILES.get('foto_produto')
        produto.data_produto = request.POST.get('data_produto')
        produto.categoria = request.POST.get('categoria')
        produto.save()


    context = {
        'produto': produto

    }
    return render(request, 'editar-produto.html')

def editar_usuario(request):
    return render(request, 'editar-usuario.html')

def registrar_usuario(request):
    return render(request, 'auth-register.html')

def registrar_produto(request):

    if request.method == 'POST':
        produto = Produto()
        produto.nome = request.POST.get('nome')
        produto.email = request.POST.get('email')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.foto_produto = request.FILES.get('foto_produto')
        produto.data_produto = request.POST.get('data_produto')
        produto.categoria = request.POST.get('categoria')
        produto.save()

    return render(request, 'registrar-produtos.html')