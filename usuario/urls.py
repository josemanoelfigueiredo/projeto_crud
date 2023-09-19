from django.urls import path
from . import views

urlpatterns = [
    path('', views.login ),
    path('cadastrar_usuario', views.cadastro_usuario)

]