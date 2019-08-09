from django.db import models


class Inventory(models.Model):
    water = models.PositiveIntegerField(default=0)
    food = models.PositiveIntegerField(default=0)
    medication = models.PositiveIntegerField(default=0)
    ammunition = models.PositiveIntegerField(default=0)

    @property
    def points(self):
        return self.water * 4 + self.food * 3 + self.medication * 2 + self.ammunition
