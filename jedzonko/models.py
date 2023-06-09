from datetime import datetime
from django.db import models
from enum import Enum


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()
    created = models.DateField(default=datetime.now())
    updated = models.DateField(default=datetime.now())
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.name


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
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    day_name = models.ForeignKey(DayName, on_delete=models.CASCADE)
