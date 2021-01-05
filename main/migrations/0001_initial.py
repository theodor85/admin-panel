# Generated by Django 3.0.8 on 2020-12-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок страницы')),
                ('coord_latitude', models.FloatField(verbose_name='Координата на карте: широта')),
                ('coord_longitude', models.FloatField(verbose_name='Координата на карте: долгота')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
            },
        ),
    ]
