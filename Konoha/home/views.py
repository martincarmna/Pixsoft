from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(request):
    return render (request, 'login.html')

def home(request):
    return render (request, 'index.html')
def loginuser(request):
    return render (request, 'loginuser.html')
def arriendos(request):
    return render (request, 'arriendos.html')
