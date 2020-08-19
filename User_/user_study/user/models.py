from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExtraUserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    something = models.TextField(blank=True)