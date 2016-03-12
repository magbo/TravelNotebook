from django.contrib import admin
from .models import Trip, Tag, Post

admin.register(Trip, Tag, Post)(admin.ModelAdmin)


# Register your models here.
