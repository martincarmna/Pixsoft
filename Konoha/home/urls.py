from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index.html'),
    path('loginuser/', views.loginuser, name='loginuser.html'),
    path('pedidos.html', views.pedidos, name='pedidos'),
    path('arriendos.html', views.arriendos, name='arriendos'),
    path('ayuda/', views.ayuda, name='ayuda.html'),

]
