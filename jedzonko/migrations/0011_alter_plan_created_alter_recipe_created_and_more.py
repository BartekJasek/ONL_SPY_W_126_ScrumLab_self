# Generated by Django 4.1.5 on 2023-02-13 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0010_plan_votes_alter_plan_created_alter_recipe_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 19, 4, 2, 277215)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 19, 4, 2, 276876)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 19, 4, 2, 276887)),
        ),
    ]
