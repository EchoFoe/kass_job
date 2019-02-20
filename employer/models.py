from django.db import models
from django.utils import timezone


class Employer(models.Model):

    first_name = models.CharField(max_length=128, verbose_name='Имя')
    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    email = models.EmailField(max_length=128, verbose_name='Почта')
    town = models.CharField(max_length=128, verbose_name='Город')
    employer_phone = models.CharField(max_length=68, verbose_name='Телефон')
    employer_organization = models.CharField(max_length=128, verbose_name='Название организации')
    employer_message = models.TextField(blank=True, null=True, default=None, verbose_name='Сообщение')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата заявки')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
        return "Работодатель %s, email: %s, телефон: %s" % (self.first_name, self.email, self.employer_phone)

    class Meta:
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатели'