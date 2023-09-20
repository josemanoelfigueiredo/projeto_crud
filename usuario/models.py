from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usuario(models.Model):
    foto_usuario = models.ImageField(null = True, blank = True,upload_to='usuario')
    nome_usuario = models.CharField(max_length= 80, null = True, blank = True)
    user = models.OneToOneField(
        User,
        on_delete= models.CASCADE,
    )
