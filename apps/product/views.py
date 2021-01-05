from django.shortcuts import render
from django.views.generic import ListView

from apps.product.models import Product


class ListProductView(ListView):
    model = Product
    template_name = 'product/product_list.html'
