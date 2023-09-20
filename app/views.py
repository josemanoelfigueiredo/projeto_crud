from django.shortcuts import redirect, render
from .models import Produto
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
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

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='login')
def editar_produto(request, id):
    produto = Produto.objects.get(id_produto=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        foto_produto = request.FILES.get('foto_produto')
        data_produto = request.POST.get('data_produto')
        categoria = request.POST.get('categoria')

        
        produto.nome = nome
        produto.email = email
        produto.descricao = descricao
        produto.preco = preco
        produto.foto_produto = foto_produto
        produto.data_produto = data_produto
        produto.categoria = categoria
        produto.save()

    context = {
        'produto': produto

    }

    return render(request, 'editar-produto.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def deletar_produto(request, id):
    
    produto = Produto.objects.get(id_produto=id)
    produto.delete()
    return redirect('meus_produtos')

def handler404(request, exception):
    return render(request, "error-404.html")