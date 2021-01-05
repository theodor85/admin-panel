from django.contrib import admin

from .models import MainPage, Image


class ImageAdmin(admin.StackedInline):
    model = Image
    extra = 1


class MainPageAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin, ]


admin.site.register(MainPage, MainPageAdmin)
