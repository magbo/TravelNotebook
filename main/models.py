from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Trip(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Tag(models.Model):
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.value


class Post(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    url = models.URLField(max_length=150, blank=True, null=True)
    tags = models.ManyToManyField(Tag)


    #tags are in post rather than tag is having posts

    def __str__(self):
        return self.title


