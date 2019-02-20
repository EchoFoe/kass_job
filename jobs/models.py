from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone
import PIL as pillow

class JobCategory(models.Model):

    name = models.CharField(max_length=128, blank=True, null=True, default=True, verbose_name='Наименование категории')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория вакансии'
        verbose_name_plural = 'Категории вакансий'

class Job(models.Model):

    name = models.CharField(max_length=512, blank=True, null=True, default=True, verbose_name='Наименование вакансии')
    price = models.DecimalField(max_digits=15, decimal_places=0, default=True, verbose_name='Оплата труда')
    education = models.CharField(max_length=128, blank=True, null=True, default=True, verbose_name='Наличие образования')
    # price_with_discount = models.DecimalField(max_digits=10, decimal_places=2, default=True)
    category = models.ForeignKey(JobCategory, blank=True, null=True, default=True, on_delete=models.CASCADE, verbose_name='Категория вакансии')
    short_description = models.TextField(max_length=50, blank=True, null=True, default=None, verbose_name='Краткое описание вакансии')
    description = models.TextField(blank=True, null=True, default=True, verbose_name='Полное описание вакансии')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')


    def description_S(self):
        return truncatechars(self.description, 30)
    def __str__(self):
            return "%s" % (self.description)


    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

class JobImage(models.Model):
    Job = models.ForeignKey(Job, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Категория вакансии')
    image = models.ImageField(upload_to='jobs_images/', verbose_name='Фотография')
    is_main = models.BooleanField(default=False, verbose_name='Главная')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')
    def __str__(self):
            return "%s" % (self.id)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'