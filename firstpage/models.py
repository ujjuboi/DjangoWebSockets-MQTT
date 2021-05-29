from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.CharField(max_length = 8, unique = True)
    flag = models.BooleanField(default=False)
    