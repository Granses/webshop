from django.db import models


class Profile(models.Model):
    external_id = models.PositiveIntegerField(verbose_name="Зовнішній Id")
    name = models.CharField(verbose_name="Імя користувача", max_length=128)

    def __str__(self):
        return f'#{self.external_id} {self.name}'

    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профілі'


class Message(models.Model):
    profile = models.ForeignKey(Profile, verbose_name="Профіль", on_delete=models.PROTECT)
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(verbose_name="Дата отримання", auto_now_add=True)

    def __str__(self):
        return f'Повідомлення {self.pk} від {self.profile}'

    class Meta:
        verbose_name = 'Півідомлення'
        verbose_name_plural = 'Повідомлення'
