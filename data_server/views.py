from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return redirect('/admin')
    else:
        if request.META.get('HTTP_REFERER') == "http://127.0.0.1:8000/":
            return render(request, 'home/home.html', context={'message': 'Login failed'})
        else:
            return render(request, 'home/home.html')


def login_webpage(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin')
    else:
        return redirect('/')
