from django.urls import path
from django.conf.urls import url
from .views import second, sensorData

urlpatterns = [
    path('', second, name = 'second'),
    path('<id>/',sensorData, name = 'dis'),
]
