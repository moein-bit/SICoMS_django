from django.db import models
from django.utils import timezone
# Create your models here.

class Workshop(models.Model):

    title = models.CharField(max_length=500)
    description = models.TextField()
    photo = models.ImageField(default='workshop_default.png',
                              upload_to='workshop_pics')
    when = models.DateTimeField()
    where = models.CharField(max_length=500)
    duration = models.TimeField()
    cost = models.BigIntegerField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title