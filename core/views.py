from django.shortcuts import render, get_object_or_404
from django.views import generic
from core.models import Product, Feedback, Category


def category_list_view(request):
    template_name = 'core/category_list.html'
    items = Category.objects.all()
    return render(request, template_name, context={'category_list': items})


def product_detail_view(request, slug, category_product_list_view):
    template_name = 'core/product_detail.html'
    product = get_object_or_404(Product, slug=slug)
    product_category = get_object_or_404(Category, slug=category_product_list_view)
    ancestor = product_category.get_ancestors(ascending=True, include_self=False)


    feedbacks = product.feedback.filter(active=True).all()

    return render(request, template_name=template_name, context={
        'product': product,
        'product_category': product_category,
        'ancestor_categorys': ancestor,
    })


def category_product_list_view(request, category):
    template_name = 'core/filtered_product_list.html'
    product_category = get_object_or_404(Category, slug=category)

    list_product = Product.objects.filter(status=1, category=product_category.id).all()
    children = product_category.get_descendants()

    return render(request, template_name=template_name, context={
        'сategory': Category,
        'product_list': list_product,
        'category_slug': product_category.slug,
        'children_categorys': children,
    })
