from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index.html'),
    path('login/', views.login, name='login.html'),
    path('home/', views.home, name='home.html'),
    path('loginuser/', views.loginuser, name='loginuser.html'),
    path('arriendos/', views.arriendos, name='arriendos.html'),
]