from django.shortcuts import render
from . import models


# Create your views here

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    return render(request,"User/login.html")

def register(request):
    return render(request,"User/register.html")