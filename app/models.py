from datetime import datetime
from django.db import models

class Produto(models.Model):
    nome = models.CharField(verbose_name='Nome do produto', max_lenght = 200)
    descricao = models.TextField()
    preco = models.IntegerField()
    foto_produto = models.ImageField(upload_to='fotos/%d/%m/%y/')
    data_produto = models.DateTimeField(default= datetime.now)
