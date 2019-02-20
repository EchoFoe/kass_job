from django.db import models
from django.utils import timezone
from django.template.defaultfilters import truncatechars


class Job_seeker(models.Model):

    first_name = models.CharField(max_length=128, verbose_name='Имя')
    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    email = models.EmailField(max_length=128, verbose_name='Почта')
    town = models.CharField(max_length=128, verbose_name='Город')
    job_seeker_phone = models.CharField(max_length=68, verbose_name='Телефон')
    job_seeker_specialty = models.CharField(max_length=128, verbose_name='Специальность')
    job_seeker_message = models.TextField(blank=True, null=True, default=None, verbose_name='Сообщение')
    is_active = models.BooleanField(default=False, verbose_name='Актуально')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата подачи заявки')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования записи')

    def __str__(self):
        return "Соискатель %s, email: %s, телефон: %s" % (self.first_name, self.email, self.job_seeker_phone)

    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'