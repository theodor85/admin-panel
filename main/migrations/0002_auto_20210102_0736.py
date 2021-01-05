# Generated by Django 3.1.4 on 2021-01-02 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='description',
            field=models.TextField(default='', verbose_name='Тег description'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='head',
            field=models.CharField(default='', max_length=255, verbose_name='Заголовок первого уровня'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='keywords',
            field=models.TextField(default='', verbose_name='Тег keywords'),
        ),
    ]