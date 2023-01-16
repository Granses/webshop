from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', context={
        'title': 'Головна'
    })


def about(request):
    return render(request, 'home/about.html', context={
        'title': 'Про сайт'
    })


def contacts(request):
    return render(request, 'home/contacts.html', context={
        'title': 'Контакти'
    })


def feedback(request):
    return render(request, 'home/feedback.html', context={
        'title': 'Зворотній звазок'
    })


def policy(request):
    return render(request, 'home/policy.html', context={
        'title': 'Політика безпеки'
    })
