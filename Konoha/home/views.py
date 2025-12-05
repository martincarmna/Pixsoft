from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render (request, 'index.html')

def index(request):
    return render (request, 'index.html')

def loginuser(request):
    return render (request, 'loginuser.html')


def categorias(request):
    return render (request, 'categorias.html')

def pedidos(request):
    return render (request, 'pedidos.html')

def arriendos(request):
    return render (request, 'arriendos.html')


def ayuda(request):
    return render (request, 'ayuda.html')

