from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index.html'),
    path('loginuser/', views.loginuser, name='loginuser.html'),
    path('pedidos/', views.pedidos, name='pedidos.html'),
    path('arriendos.html', views.arriendos, name='arriendos'),
    path('productos.html', views.productos, name='productos'),

]
