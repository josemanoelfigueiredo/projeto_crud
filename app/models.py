from django.db import models
from datetime import datetime


class Produto(models.Model):
    id_produto = models.IntegerField(primary_key= True)
    nome = models.CharField(verbose_name='Nome do produto', max_length = 200, null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    descricao = models.TextField(null = True, blank = True)
    preco = models.FloatField(null = True, blank = True)
    foto_produto = models.ImageField(upload_to='fotos/%d/%m/%y/', null = True)
    data_produto = models.DateTimeField(default= datetime.now, null = True, blank = True)
    categoria = models.TextField(max_length = 62, null = True, blank = True)


