from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):

    MAJORS = (
        ('MED', "Medicine"),
        ('OTH', 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_default.jpg',
                              upload_to='profile_pics')
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    major = models.CharField(max_length=3, 
                             choices=MAJORS, 
                             null=True)
    semester = models.SmallIntegerField(null=True)
    student_id = models.CharField(max_length=12, null=True)
    university = models.CharField(max_length=60, null=True)

    def __repr__(self):
        return f"{self.user.username} Profile"
