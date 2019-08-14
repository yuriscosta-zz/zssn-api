from django.db import models


class Location(models.Model):
    latitude = models.FloatField(null=True, default=None)
    longitude = models.FloatField(null=True, default=None)
