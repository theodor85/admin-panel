# Generated by Django 3.1.4 on 2021-01-05 05:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('products', '0001_initial'), ('products', '0002_product_date_added'), ('products', '0003_auto_20210103_0538'), ('products', '0004_auto_20210103_0539'), ('products', '0005_list'), ('products', '0006_listitem')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, default=' ', max_length=255, null=True, verbose_name='Название продукта')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение продукта')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок страницы')),
                ('keywords', models.TextField(blank=True, default='', null=True, verbose_name='Тег keywords')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Тег description')),
                ('slug', models.SlugField(verbose_name='URL-адрес')),
                ('date_added', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=255, verbose_name='Заголовок списка')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='products.product')),
            ],
            options={
                'verbose_name': 'Список',
                'verbose_name_plural': 'Списки',
            },
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Текст пункта')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='products.list')),
            ],
            options={
                'verbose_name': 'Пункт списка',
                'verbose_name_plural': 'Пункты списка',
            },
        ),
    ]