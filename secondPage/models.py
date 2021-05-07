from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SensorData(models.Model):
    sensorName = models.CharField(max_length = 50)

class UserSensor(models.Model):
    Uid = models.ForeignKey(User, on_delete=models.CASCADE)
    Sid = models.ForeignKey(SensorData, on_delete=models.CASCADE)