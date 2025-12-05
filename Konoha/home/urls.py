from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index.html'),
    path('loginuser/', views.loginuser, name='loginuser.html'),
    path('arriendos/', views.arriendos, name='arriendos.html'),
]
