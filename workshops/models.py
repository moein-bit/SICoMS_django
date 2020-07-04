from django.db import models
from django.utils import timezone


class Workshop(models.Model):

    title = models.CharField(max_length=500)
    summary = models.TextField(default="New Workshop")
    description = models.TextField()
    photo = models.ImageField(default='workshop_default.png',
                              upload_to='workshop_pics')
    when = models.DateTimeField()
    where = models.CharField(max_length=500)
    duration = models.CharField(max_length=50, default="2 hrs")
    cost = models.BigIntegerField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title