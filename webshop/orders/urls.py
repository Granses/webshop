from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^bill/(?P<sel_list>[0-9\,]{3,})$', bill),
    re_path(r'^confirm/(?P<init_list>[0-9\,]{3,})$', confirm)
]
