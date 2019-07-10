from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Event(models.Model):
    title = models.CharField(max_length=256)
    presenter = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    time = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    dress_code = models.CharField(max_length=128, blank=True)