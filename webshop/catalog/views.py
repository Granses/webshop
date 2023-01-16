from django.shortcuts import render
from .models import Category
from .models import Producer
from .models import Product
from django.core.paginator import Paginator


def index(request):
    page_size = 3
    all_categories = Category.objects.all()
    all_products = Product.objects.all()

    paginator = Paginator(all_products, page_size)
    page_number = request.GET.get('page')
    paginate_products = paginator.get_page(page_number)

    return render(request, 'catalog/index.html', context={
        'title': 'Каталог товарів',
        'all_categories': all_categories,
        'all_producers': Producer.objects.all(),
        'all_products': all_products,
        'paginate_products': paginate_products,

    })


def details(request, prod_id):
    all_categories = Category.objects.all()
    all_products = Product.objects.all()
    return render(request, 'catalog/details.html', context={
        'title': 'Каталог товарів',
        'all_categories': all_categories,
        'all_products': all_products,
    })


def ajax_cart(request):
    login_x = request.GET.get('login')

    try:
        User.objects.get(username=login_x)
        message = 'зайнятий'
    except User.DoesNotExist:
        message = 'вільний'

    return JsonResponse({
        'message': message
    })

