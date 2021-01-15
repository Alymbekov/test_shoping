from rest_framework import generics

from apps.product.models import Product
from .serializers import ProductAPISerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAPISerializer
