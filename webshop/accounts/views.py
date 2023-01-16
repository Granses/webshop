from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_up.html', context={
            'title': 'Register'
        })
    elif request.method == 'POST':
        # Отримання даних з форми
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

        # Валідація даних
        color = 'gray'
        message = 'default'
        if pass1_x != pass2_x:
            color = 'red'
            message = 'Паролі не співпадають!'
        elif pass1_x == '':
            # Інші перевірки
            pass
        else:
            # додавання Юзера
            new_user = User.objects.create_user(login_x, email_x, pass1_x)

            # формування звіту
            if new_user is None:
                color = 'red'
                message = 'Реєстрація провалена!'
            else:
                new_user.save()
                color = 'green'
                message = 'Ви зареєструвались'
        return render(request, 'accounts/report.html', context={
            'title': 'Звіт про реєстрацію',
            'color': color,
            'message': message,
        })


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_in.html', context={
            'title': 'Вхід'
        })
    elif request.method == 'POST':
        # Отримання даних з форми
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        remember = request.POST.get('remember')

        # Переверка наявності в БД
        user = authenticate(request, username=login_x, password=pass1_x)
        if user is None:
            color = 'red'
            message = 'Користувач не знайдений!'
            return render(request, 'accounts/report.html', context={
                'title': 'Звіт про авторизацію',
                'color': color,
                'message': message,
            })

        else:
            login(request, user)
            return redirect('/home')


def sign_out(request):
    logout(request)
    return redirect('/home')


def profile(request):
    return render(request, 'accounts/profile.html', context={
        'title': 'Профіль користувача',
    })


def ajax_reg(request):
    login_x = request.GET.get('login')

    try:
        User.objects.get(username=login_x)
        message = 'зайнятий'
    except User.DoesNotExist:
        message = 'вільний'

    return JsonResponse({
        'message': message
    })


def ajax_email(request):
    email_x = request.GET.get('email')

    try:
        User.objects.get(email=email_x)
        message = 'зайнятий'
    except User.DoesNotExist:
        message = 'вільний'

    return JsonResponse({
        'message': message
    })
