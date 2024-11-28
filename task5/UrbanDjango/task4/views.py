from django.shortcuts import render


def home_view(request):
    title = 'Главная страница'
    name_home = 'Главная'
    name_store = 'Магазин'
    name_cart = 'Корзина'
    context = {
        'title': title,
        'name_home': name_home,
        'name_store': name_store,
        'name_cart': name_cart,
    }
    return render(request, 'fourth_task/home.html', context)


def games_view(request):
    title = 'Игры'
    name_home = 'Главная'
    name_store = 'Магазин'
    name_cart = 'Корзина'
    games = ['Minecraft', 'Wither 3', 'CS:GO']
    button_buy_title = 'Купить'
    context = {
        'title': title,
        'name_home': name_home,
        'name_store': name_store,
        'name_cart': name_cart,
        'games': games,
        'button_buy_title': button_buy_title,
    }
    return render(request, 'fourth_task/games.html', context)


def cart_view(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    name_home = 'Главная'
    name_store = 'Магазин'
    name_cart = 'Корзина'
    context = {
        'title': title,
        'name_home': name_home,
        'name_store': name_store,
        'name_cart': name_cart,
        'text': text,
    }
    return render(request, 'fourth_task/cart.html', context)