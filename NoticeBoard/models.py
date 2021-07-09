from django.db import models

# Create your models here.
class message(models.Model):
    organiser = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    topic = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()