from django.shortcuts import render
from .models import Produto

def index(request):
    return render(request, 'index.html')


def registrar_produto(request):

    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    preco = request.POST.get('preco')
    foto_produto = request.POST.get('foto_produto')
    data_produto = request.POST.get('data_produto')

    produto = Produto(
        nome = nome,
        descricao = descricao,
        preco = preco,
        foto_produto = foto_produto,
        data_produto = data_produto
    )

    produto.save()

    return render(request, "registrar-produtos.html")