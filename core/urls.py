from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.category_list_view, name='category_list'),
    path('category/<slug:category>', views.category_product_list_view, name='category_products'),
    path('<slug:category_product_list_view>/<slug:slug>', views.product_detail_view, name='product_detail'),
]
