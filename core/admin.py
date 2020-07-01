from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', ]

    fields = [
        'name', 'parent', 'slug',
    ]


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'status', 'created_on')


admin.site.register(Product, ProductAdmin)
