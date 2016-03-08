from django.db import models
from django.utils import timezone


class Trip(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    country = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Post(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.title
