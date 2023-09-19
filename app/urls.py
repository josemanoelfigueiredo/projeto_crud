from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_produto, name='registrar_produto'),
    path('editar_produto/', views.editar_produto, name = 'editar_produto' ),
    path('editar_usuario/<int:id_produto>/', views.editar_usuario, name = 'editar_usuario' ),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('meus_produtos/', views.meus_produtos, name='meus_produtos')
]