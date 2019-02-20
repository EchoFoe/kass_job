from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    email = models.EmailField(verbose_name='E-мейл')
    name = models.CharField(max_length=128, verbose_name='Имя подписчика')
    message = models.TextField(blank=True, null=True, default=None, verbose_name='Сообщение подписчика')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата подписки')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата обновления подписки')

    def __str__(self):
        return "Подписчик %s, email: %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'