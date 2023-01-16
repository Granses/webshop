from django.contrib import admin
from .models import Message
from .models import Profile


admin.site.register(Message)
admin.site.register(Profile)
