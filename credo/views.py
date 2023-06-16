from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def account(request):
    return render(request, 'account.html')


def entrance(request):
    return render(request, 'entrance.html')


def registration(request):
    return render(request, 'registration.html')
