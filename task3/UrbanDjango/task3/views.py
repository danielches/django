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
    return render(request, 'third_task/home.html', context)

def games_view(request):
    title = 'Игры'
    game1 = 'Minecraft'
    game2 = 'Wither 3'
    game3 = 'CS:GO'
    button_buy_title = 'Купить'
    button_back_title = 'Вернуться обратно'
    context = {
        'title': title,
        'game1': game1,
        'game2': game2,
        'game3': game3,
        'button_buy_title': button_buy_title,
        'button_back_title': button_back_title,
    }
    return render(request, 'third_task/games.html', context)

def cart_view(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    button_back_title = 'Вернуться обратно'
    context = {
        'title': title,
        'text': text,
        'button_back_title': button_back_title,
    }
    return render(request, 'third_task/cart.html', context)