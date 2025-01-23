from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game
from django.db import IntegrityError


# Create your views here.

def main(request):
    title = 'Главная'
    context = {'title': title}
    return render(request, 'main.html', context)


def magazine(request):
    title = 'Наш Магазин'
    # products = [
    #     'Air Jordan', 'Dunk Low Retro', 'Adidas Super-Star II'
    # ]
    all_games = Game.objects.all()
    context = {
        'title': title,
        'all_games': all_games,
    }
    return render(request, 'magazine.html', context)


def cart(request):
    title = 'Ваша Корзина'
    cart_info = 'Ваша корзина пуста'
    context = {
        'title': title,
        'cart_info': cart_info
    }
    return render(request, 'cart.html', context)


def sign_up_by_html(request):
    # users = ['Denis', 'Katya']
    info = {}
    if request.method == 'POST':  # Проверяем метод коннекта с сервером
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # print(f'Username: {username}')
        # print(f'Password: {password}')
        # print(f'Repeat_Password: {repeat_password}')
        # (f'Age: {age}')

        # if password != repeat_password:
        #    info['error'] = 'Пароли не совпадают!'
        # elif int(age) < 18:
        #    info['error'] = 'Вы должны быть старше 18!'
        # elif username in users:
        #    info['error'] = 'Пользователь уже существует!'
        # else:

        try:  # Пробуем создать пользователя с переданными данными
            Buyer.objects.create(username=username, balance=0, age=age)
            info['register'] = f'Пользователь {username}, зарегистрирован!'
            return render(request, 'registration_page.html', info)
        except IntegrityError:  # Обработка ошибки
            info['register'] = 'Пользователь уже существует'
            return render(request, 'registration_page.html', info)

    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    # users = ['Denis', 'Katya']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # if password != repeat_password:
            #    info['error'] = 'Пароли не совпадают'
            # elif int(age) < 18:
            #    info['error'] = 'Вы должны быть старше 18'
            # elif username in users:
            #    info['error'] = 'Пользователь уже существует'
            # else:

            try:  # Пробуем создать пользователя с переданными данными
                Buyer.objects.create(username=username, balance=0, age=age)
                info['register'] = f'Пользователь {username}, зарегистрирован!'
                return render(request, 'registration_page.html', info)
            except IntegrityError:  # Обработка ошибки
                info['register'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', info)

    return render(request, 'registration_page.html', info)
