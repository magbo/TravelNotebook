from django.contrib import admin
from .models import Trip, Post

admin.register(Trip, Post)(admin.ModelAdmin)


# Register your models here.
