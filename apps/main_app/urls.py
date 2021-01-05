from django.urls import path
from apps.main_app import views


urlpatterns = [
    #CBV-ClassBasedView
    path('', views.IndexPageView.as_view(), name='index'),
]

