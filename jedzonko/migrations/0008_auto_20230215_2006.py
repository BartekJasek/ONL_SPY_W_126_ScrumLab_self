# Generated by Django 2.2.6 on 2023-02-15 19:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0007_auto_20230209_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 20, 6, 46, 352942)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 20, 6, 46, 352742)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 20, 6, 46, 352752)),
        ),
    ]