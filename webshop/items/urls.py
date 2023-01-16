from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('wish', wish),
    path('ajax_cart', ajax_cart),
    path('ajax_wish', ajax_wish),
    path('ajax_cart_display', ajax_cart_display),
    path('ajax_del_item', ajax_del_item),
    path('ajax_del_wish', ajax_del_wish),
]
