# Generated by Django 3.1.4 on 2021-01-03 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210103_0539'),
    ]

    operations = [
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
    ]
