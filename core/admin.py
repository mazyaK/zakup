from django.contrib import admin
from .models import Category, Product, Feedback


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', ]

    fields = [
        'name', 'parent', 'slug',
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'created_on')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'created_on', 'active')
    list_filter = ('active', 'created_on', 'updated_on')
    search_fields = ('name', 'body')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Feedback, FeedbackAdmin)
