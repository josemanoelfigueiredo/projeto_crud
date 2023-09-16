from django.db import models
from datetime import datetime


class Produto(models.Model):
    nome = models.CharField(verbose_name='Nome do produto', max_length = 200, null = False)
    descricao = models.TextField(null = False)
    preco = models.IntegerField(null = False)
    foto_produto = models.ImageField(upload_to='fotos/%d/%m/%y/', blank = True)
    data_produto = models.DateTimeField(default= datetime.now, null = False)
