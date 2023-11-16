from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registration successful')
            return redirect('registration-url')
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})


def login(request):
    return render(request, 'auth/login.html')


def logout(request):
    return render(request, 'auth/logout.html')
