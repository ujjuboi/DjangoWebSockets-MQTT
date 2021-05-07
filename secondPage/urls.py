from django.urls import path
from django.conf.urls import url
from .views import second

urlpatterns = [
    path('', second, name = 'second'),
]
