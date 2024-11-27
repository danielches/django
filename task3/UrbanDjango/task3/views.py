from django.shortcuts import render

def home_view(request):
    return render(request, 'third_task/home.html')

def games_view(request):
    return render(request, 'third_task/games.html')

def cart_view(request):
    return render(request, 'third_task/cart.html')