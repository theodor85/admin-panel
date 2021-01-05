from django.db import models

from .validators import validate_format, validate_max_file_size


class MainPage(models.Model):
    title = models.CharField(
        verbose_name='Заголовок страницы',
        max_length=255,
        blank=False,
        null=False,
    )
    head = models.CharField(
        verbose_name='Заголовок первого уровня',
        max_length=255,
        blank=True,
        null=True,
        default='',
    )
    text = models.TextField(
        verbose_name='Текст под слайдером',
        blank=True,
        null=True,
        default='',
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
    coord_latitude = models.FloatField(
        verbose_name='Координата на карте: широта',
        blank=True,
        null=True,
        default=0,
    )
    coord_longitude = models.FloatField(
        verbose_name='Координата на карте: долгота',
        blank=True,
        null=True,
        default=0,
    )

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    def __str__(self):
        return f'Главная страница: {self.title}'


class Image(models.Model):

    page = models.ForeignKey(
        MainPage,
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(
        verbose_name='Файл изображения',
        validators = [validate_format, validate_max_file_size],
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Описание (содержимое атрибута alt)',
        blank=True,
        null=True,
        default='',
    )

    class Meta:
        verbose_name = 'Изображение на главной странице'
        verbose_name_plural = 'Изображения на главной странице'

    def __str__(self):
        return f'''Изображение: {self.image}'''
