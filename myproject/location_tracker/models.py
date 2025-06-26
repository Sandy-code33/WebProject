from django.db import models

class Location(models.Model):
    user_id = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

