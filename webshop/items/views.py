from django.shortcuts import render
from django.http import JsonResponse
from .models import Item, Wish


def index(request):
    return render(request, 'items/index.html', {
        'title': 'Перегляд кошика',
        'user_items': Item.objects.filter(user_id=request.user.id)
    })


def ajax_cart(request):
    response = dict()

    # 1 - Отримую значення GET-параметрів із AJAX-запиту:
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')
    price = request.GET.get('price')

    # 2 - Тестова перевірка
    response['uid'] = f'UID: {uid}'
    response['pid'] = f'PID: {pid}'
    response['price'] = f'price: {price}'

    # 3 - Зберігаю товар доданий в кошик, у базі даних
    Item.objects.create(
        user_id=uid,
        product_id=pid,
        status='Очікування замовлення'
    )
    response['create_mess'] = 'Товар додано'

    # 4 - Зчитую з бази список товарів даного користувача:
    user_items = Item.objects.filter(user_id=uid)

    # 5 - Загальна вартість всіх товарів користувача:
    amount = 0
    for item in user_items:
        amount += item.product.price

    # 6 - Відповіть сервера про загальну кільість та вартість товарів користувача:
    response['count'] = len(user_items)
    response['amount'] = amount

    # 7 - Відправляю відповідь клієнту:

    return JsonResponse(response)


def wish(request):
    return render(request, 'items/wish.html', {
        'title': 'Перегляд обраного',
        'user_wish': Wish.objects.filter(user_id=request.user.id)
    })


def ajax_wish(request):
    response = dict()
    uid = request.GET.get('uid')
    wid = request.GET.get('wid')
    response['uid'] = f'UID: {uid}'
    response['wid'] = f'wID: {wid}'
    response['test_mess'] = 'TEST'
    Wish.objects.create(
        user_id=uid,
        product_id=wid
    )
    user_items = Wish.objects.filter(user_id=uid)
    response['count'] = len(user_items)
    return JsonResponse(response)


def ajax_cart_display(request):

    uid = request.GET['uid']
    user_items = Item.objects.filter(user_id=uid)
    user_wish = Wish.objects.filter(user_id=uid)

    s = 0
    for item in user_items:
        s += item.product.price

    return JsonResponse({
        'uid_back': uid,
        'amount': s,
        'count': len(user_items),
        'wish_count': len(user_wish)
    })


def ajax_del_item(request):
    item_id = request.GET['item_id']
    del_item = Item.objects.get(id=item_id)
    del_item.delete()
    return JsonResponse({
        'report': f'Товар із ID: {item_id} був видалений із кошика!'
    })


def ajax_del_wish(request):
    item_id = request.GET['item_id']
    del_item = Wish.objects.get(id=item_id)
    del_item.delete()
    return JsonResponse({
        'report': f'Товар із ID: {item_id} був доданий в кошик та видалений з обраного!'
    })
