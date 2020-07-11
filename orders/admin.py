from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created_on', 'updated_on']

    list_filter = ['paid', 'created_on', 'updated_on']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
