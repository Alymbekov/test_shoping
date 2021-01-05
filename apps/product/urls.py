from django.urls import path

from apps.product import views

app_name = 'product'

urlpatterns = [
    path('', views.ListProductView.as_view(), name='product_list'),
]
