from django.db import models
from items.models import Item
from django.contrib.auth.models import User
from django.utils import timezone


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(null=False, default=timezone.now)
    complete = models.DateTimeField(null=True)
    status = models.CharField(max_length=100)
    amount = models.IntegerField()


class Purchase(models.Model):
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.item.product.name}'
