from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
