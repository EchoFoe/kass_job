# Generated by Django 2.1.4 on 2019-02-15 13:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата заявки'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='email',
            field=models.EmailField(max_length=128, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='employer_message',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='employer_organization',
            field=models.CharField(max_length=128, verbose_name='Название организации'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='employer_phone',
            field=models.CharField(max_length=68, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='first_name',
            field=models.CharField(max_length=128, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='last_name',
            field=models.CharField(max_length=128, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='town',
            field=models.CharField(max_length=128, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата редактирования'),
        ),
    ]
