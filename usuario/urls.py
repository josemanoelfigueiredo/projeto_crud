from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login" ),
    path('registrar_usuario/', views.registrar_usuario, name="registrar_usuario"),
    path('editar_usuario/', views.editar_usuario, name="editar_usuario"),
    path('logout/', views.logout, name ="logout"),
]