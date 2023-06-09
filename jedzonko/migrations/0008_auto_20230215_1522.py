# Generated by Django 2.2.6 on 2023-02-15 14:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0007_auto_20230215_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 15, 22, 38, 175513)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 15, 22, 38, 175052)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 15, 22, 38, 175072)),
        ),
        migrations.AlterField(
            model_name='recipeplan',
            name='day_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.DayName'),
        ),
        migrations.AlterField(
            model_name='recipeplan',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.Plan'),
        ),
        migrations.AlterField(
            model_name='recipeplan',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.Recipe'),
        ),
    ]
