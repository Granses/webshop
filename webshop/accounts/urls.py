from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up', sign_up),
    path('sign_out', sign_out),
    path('profile', profile),
    path('sign_in', sign_in),
    path('ajax_reg', ajax_reg),
    path('ajax_email', ajax_email),
]
