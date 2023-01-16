from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User
from django.utils import timezone


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, default=timezone.now)
    status = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.user} / {self.product}  :: {self.date}'


class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user} / {self.product}'

