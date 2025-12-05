# Konoha/urls.py
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # AGREGAR ESTA LÍNEA:
    path('', include('home.urls')), 
    
]