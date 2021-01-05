from django.db import models


class Product(models.Model):

    product_name = models.CharField(
        max_length=255,
        verbose_name='Название продукта',
        blank=True,
        null=True,
        default=' ',
    )
    date_added = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
    )
    photo = models.ImageField(
        verbose_name='Изображение продукта',
        null=True,
        blank=True,
    )
    title = models.CharField(
        verbose_name='Заголовок страницы',
        max_length=255,
        blank=False,
        null=False,
    )
    keywords = models.TextField(
        verbose_name='Тег keywords',
        blank=True,
        null=True,
        default='',
    )
    description = models.TextField(
        verbose_name='Тег description',
        blank=True,
        null=True,
        default='',
    )
    slug = models.SlugField(
        verbose_name='URL-адрес',
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.product_name}' if self.product_name else self.slug


class List(models.Model):
    head = models.CharField(
        verbose_name='Заголовок списка',
        max_length=255,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='lists',    
    )

    def __str__(self):
        product = f'{self.product.product_name}' \
            if self.product.product_name \
            else self.product.slug
        return f'Список: "{self.head}" продукта {product}'

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'


class ListItem(models.Model):
    text = models.CharField(
        verbose_name='Текст пункта',
        max_length=255,
    )
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name='items',    
    )

    def __str__(self):
        return f'Пункт списка: {self.text}'

    class Meta:
        verbose_name = 'Пункт списка'
        verbose_name_plural = 'Пункты списка'    
