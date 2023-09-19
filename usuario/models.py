from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    foto = models.ImageField(null = True, blank = True,upload_to='usuario')
    user = models.OneToOneField(
        User,
        on_delete= models.CASCADE,
    )
