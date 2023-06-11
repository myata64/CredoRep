from django.shortcuts import render, redirect


def account(request):
    return render(request, 'account.html')


def home(request):
    return render(request, 'home.html')
