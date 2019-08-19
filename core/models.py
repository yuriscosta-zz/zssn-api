from django.db import models

from locations.models import Location
from inventories.models import Inventory


class Survivor(models.Model):
    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    infected_reports = models.PositiveIntegerField(default=0)
    is_infected = models.BooleanField(default=False)
    last_location = models.ForeignKey(Location,
                                      on_delete=models.CASCADE,
                                      null=True,
                                      blank=True)
    inventory = models.ForeignKey(Inventory,
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True)

    def save(self, *args, **kwargs):
        self.is_infected = True if self.infected_reports >= 3 else False
        super(Survivor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
