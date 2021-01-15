from django.urls import path, include

from apps.product import views

app_name = 'product'

urlpatterns = [
    path('', views.ListProductView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product-api/', include('apps.product.api.urls')),
]

#<str:slug>
#<uuid:key>

