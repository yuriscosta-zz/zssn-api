from django.db import models
from django.utils import timezone

from core.models import Survivor


class FlagInfected(models.Model):
    author = models.ForeignKey(Survivor,
                               on_delete=models.CASCADE,
                               related_name='author')
    target = models.ForeignKey(Survivor,
                               on_delete=models.CASCADE,
                               related_name='target')
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.author != self.target:
            flags = FlagInfected.objects.filter(author=self.author, target=self.target).all()
            if len(flags) == 0:
                self.target.infected_reports += 1
                self.target.save()
                super(FlagInfected, self).save(*args, **kwargs)

    def __str__(self):
        return '{} flagged {}'.format(self.author, self.target)
