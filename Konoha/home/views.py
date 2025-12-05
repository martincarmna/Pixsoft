from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'index.html')

def loginuser(request):
    return render(request, 'loginuser.html')
