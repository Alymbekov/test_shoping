from django.contrib.postgres.search import TrigramSimilarity
from django_filters import rest_framework as filters
from rest_framework import generics

from apps.product.models import Product
from .paginations import CustomOffsetPagination
from .serializers import ProductAPISerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAPISerializer
    pagination_class = CustomOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'in_stock', 'featured')

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.annotate(
                similarity=TrigramSimilarity('title', search_query),
            ).filter(similarity__gt=0.2).order_by('-similarity')
        return queryset



