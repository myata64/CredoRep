from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password


def home(request):
    return render(request, 'home.html')


def account(request):
    return render(request, 'account.html')


def entrance(request):
    return render(request, 'entrance.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if confirm_password != password:
            messages.error(request, 'Пароли не совпадают.')
            return redirect('register')

        hashed_password = make_password(password)
        User.objects.create(email=email, password=hashed_password)

        messages.success(request, 'Регистрация прошла успешно.')
        return redirect('home')

    return render(request, 'registration.html')
