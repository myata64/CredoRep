from django.shortcuts import render, redirect
# from django.contrib.auth.forms import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from .models import User, Product
from .forms import UserForm


def home(request):
    return render(request, 'home.html')


def account(request):
    user = request.user
    if request.method == 'POST':
        User.objects.get(username=request.POST.get('username'))
        User.objects.get(phone_number=request.POST.get('phone_number'))
        user.phone_number = request.POST.get('phone_number')
        user.email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if confirm_password != new_password:
            error_message = 'Пароли не совпадают'
            return render({'error_message': error_message})
        else:
            hashed_password = make_password(password=new_password)
            User.objects.get(password=hashed_password)
            user.save()
            return redirect('account')
    return render(request, 'account.html')


def entrance(request):
    return render(request, 'entrance.html')


def shoes(request):
    products = Product.objects.all()
    return render(request, 'shoes.html', {'products': products})


def newbalance(request):
    return render(request, 'nb990.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Проверка на существование почты в БД
        if User.objects.filter(email=email).exists():
            error_message = 'Пользователь уже существует'
            return redirect('register', {'error_message': error_message})
        # Проверка на совпадение паролей
        if confirm_password != password:
            messages.error(request, 'Пароли не совпадают.')
            return redirect('register')
        else:
            hashed_password = make_password(password)
            User.objects.create(username=email, email=email, password=hashed_password)
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)

        messages.success(request, 'Регистрация прошла успешно.')
        return redirect('home')

    return render(request, 'registration.html')


@csrf_protect
def entrance(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Неправильное имя пользователя или пароль'
            return render(request, 'entrance.html', {'error_message': error_message})
    else:
        return render(request, 'entrance.html')


def logout_view(request):
    logout(request)
    return redirect('home')
