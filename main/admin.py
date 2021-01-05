from django.contrib import admin

from .models import MainPage, Paragraph, Image


class ParagraphAdmin(admin.StackedInline):
    model = Paragraph
    extra = 1


class ImageAdmin(admin.StackedInline):
    model = Image
    extra = 1


class MainPageAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin, ParagraphAdmin]


admin.site.register(MainPage, MainPageAdmin)
