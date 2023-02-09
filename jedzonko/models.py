from datetime import datetime
from django.db import models
from enum import Enum


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
    recipes = models.ManyToManyField(Recipe, through='RecipePlan')

class DayName(models.Model):
    name = models.CharField(max_length=128)
    order = models.IntegerField(default=0)

class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=128)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    day_name = models.OneToOneField(DayName, on_delete=models.CASCADE)






