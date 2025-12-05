from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render (request, 'index.html')
def loginuser(request):
    return render (request, 'loginuser.html')
def pedidos(request):
    return render (request, 'pedidos.html')
def arriendos(request):
    return render (request, 'arriendos.html')
def ayuda(request):
    return render (request, 'ayuda.html')
def productos(request):
    return render (request, 'productos.html')