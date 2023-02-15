# Generated by Django 4.1.5 on 2023-02-13 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0009_alter_plan_created_alter_recipe_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 58, 33, 991893)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 58, 33, 991570)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 58, 33, 991599)),
        ),
    ]
