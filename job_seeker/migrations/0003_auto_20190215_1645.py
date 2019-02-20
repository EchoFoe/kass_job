# Generated by Django 2.1.4 on 2019-02-15 13:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker', '0002_job_seeker_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_seeker',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата подачи заявки'),
        ),
        migrations.AlterField(
            model_name='job_seeker',
            name='email',
            field=models.EmailField(max_length=128, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='job_seeker',
            name='first_name',
            field=models.CharField(max_length=128, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='job_seeker',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Актуально'),
        ),
        migrations.AlterField(
            model_name='job_seeker',
            name='job_seeker_message',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='job_seeker',
            name='job_seeker_phone',
            field=models.CharField(max_length=68, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='job_seeker',
            name='job_seeker_specialty',
            field=models.CharField(max_length=128, verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='job_seeker',
            name='last_name',
            field=models.CharField(max_length=128, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='job_seeker',
            name='town',
            field=models.CharField(max_length=128, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='job_seeker',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата редактирования записи'),
        ),
    ]