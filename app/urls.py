from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='app'),
    path('/prooduto', views.registrar_produto, name ='registro de produtos')
]