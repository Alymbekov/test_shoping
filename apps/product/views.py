from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.product.models import Product


class ListProductView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     super
    def get_queryset(self):
        return Product.objects.filter(in_stock=True)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
