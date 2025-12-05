from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   
    path('login/', views.login, name='login.html'),
    path('home/', views.home, name='home.html'),
    path('loginuser/', views.loginuser, name='loginuser.html'),
    path('categorias/', views.categorias, name = 'categorias'),
]