from django.urls import path
from apps.main_app import views

app_name = 'main_app'

urlpatterns = [
    #CBV-ClassBasedView
    path('', views.IndexPageView.as_view(), name='index'),
]

