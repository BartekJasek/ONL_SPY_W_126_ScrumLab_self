from datetime import datetime
from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=128)
    ingredients = models.TextField()
    description = models.TextField()
    created = models.DateField(default=datetime.now())
    updated = models.DateField(default=datetime.now())
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)


class Plan(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    created = models.DateField(default=datetime.now())
    votes = models.IntegerField(default=0)

