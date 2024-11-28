from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


def sign_up_by_html(request):
    users = ['danil', 'evgeny', 'kirill', 'oleg']
    info = dict()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        print(f'username {username}')
        print(f'password {password}')
        print(f'repeat_password {repeat_password}')
        print(f'age {age}')
        if password == repeat_password and age >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    users = ['danil', 'evgeny', 'kirill', 'oleg']
    info = dict()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        info['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            print(f'username {username}')
            print(f'password {password}')
            print(f'repeat_password {repeat_password}')
            print(f'age {age}')
            if password == repeat_password and age >= 18 and username not in users:
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
    else:
        form = ContactForm()
        info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

