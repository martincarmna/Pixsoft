from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   
    
    path('home/', views.home, name='index.html'),
    path('loginuser/', views.loginuser, name='loginuser.html'),
    path('categorias/', views.categorias, name = 'categorias.html'),
    path('arriendos/', views.arriendos, name='arriendos.html'),
]
