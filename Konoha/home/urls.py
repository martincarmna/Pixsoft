from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   
    
    path('home/', views.home, name='index.html'),
    path('loginuser/', views.loginuser, name='loginuser.html'),

    path('categorias/', views.categorias, name = 'categorias.html'),
    path('arriendos/', views.arriendos, name='arriendos.html'),

    path('pedidos.html', views.pedidos, name='pedidos'),
    path('arriendos.html', views.arriendos, name='arriendos'),
    path('ayuda/', views.ayuda, name='ayuda.html'),

]
