from django.urls import path
from . import views

urlpatterns = [
    path('registrar_produto/', views.registrar_produto, name='registrar_produto'),
    path('<id>/editar_produto/', views.editar_produto, name = 'editar_produto' ),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('meus_produtos/', views.meus_produtos, name='meus_produtos'),
    path('<id>/deletar_produto', views.deletar_produto, name="deletar_produto" ),
]