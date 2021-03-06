# Generated by Django 2.1.4 on 2019-02-15 13:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'Подписчик', 'verbose_name_plural': 'Подписчики'},
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата подписки'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-мейл'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='message',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Сообщение подписчика'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Имя подписчика'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата обновления подписки'),
        ),
    ]
