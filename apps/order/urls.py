from django.urls import path, include
from rest_framework import routers

from apps.order.views import OrderViewSet

router = routers.SimpleRouter()
router.register('orders', OrderViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]