from django.db import models


class Location(models.Model):
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
