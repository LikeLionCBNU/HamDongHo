from django.db import models
from django.utils import timezone

# Create your models here.

class Schedule(models.Model):
    title = models.CharField(max_length = 100)
    memo = models.TextField()
    schedule_date = models.DateTimeField(default = timezone.now)
    published_data = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return self.title