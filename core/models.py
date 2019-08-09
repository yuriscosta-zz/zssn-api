from django.db import models

from locations.models import Location


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
                                      blank=True,
                                      null=True)

    def save(self, *args, **kwargs):
        self.is_infected = True if self.infected_reports >= 3 else False
        super(Survivor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    pass


class Report(models.Model):
    pass
