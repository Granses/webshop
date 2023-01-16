from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('', index),
    path('index', index),
    path('details', details),
    path('details/<int:prod_id>/', details, name='product'),
]
