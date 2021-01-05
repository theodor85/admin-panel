from django.contrib import admin

from .models import Product, List, ListItem


class ListItemAdmin(admin.StackedInline):
    model = ListItem
    extra = 2


class ListAdmin(admin.ModelAdmin):
    list_filter = ('product', )
    inlines = [ListItemAdmin]


class ListAdminInline(admin.StackedInline):
    model = List


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added', )
    inlines = [ListAdminInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(List, ListAdmin)
