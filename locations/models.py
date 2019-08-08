from django.db import models

# from core.models import Survivor


class Location(models.Model):
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
    # survivor = models.ForeignKey(Survivor,
    #                              on_delete=models.CASCADE,
    #                              null=True,
    #                              related_name='last_location')
