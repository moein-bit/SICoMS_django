from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):

    CATEGORIES = (
        ("RES", "Research"),
        ("VIS", "Visit"),
        ("SCH", "School"),
        ("CON", "Conference"),
        ("COM", "Competition"),
    )

    title = models.CharField(max_length=100)
    photo = models.ImageField(default="post_default.jpg", upload_to="post_pics")
    category = models.CharField(max_length=3, choices=CATEGORIES, null=True)
    summary = models.TextField(max_length=500)
    explanation = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return f"the events title is: {self.title}"

    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"pk": self.pk})

