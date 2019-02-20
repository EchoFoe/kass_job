# Generated by Django 2.1.4 on 2018-12-19 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('town', models.CharField(max_length=128)),
                ('employer_phone', models.CharField(max_length=68)),
                ('employer_organization', models.CharField(max_length=128)),
                ('employer_message', models.TextField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Работодатель',
                'verbose_name_plural': 'Работодатели',
            },
        ),
    ]