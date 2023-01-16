from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about', about),
    path('contacts', contacts),
    path('feedback', feedback),
    path('policy', policy),
]
