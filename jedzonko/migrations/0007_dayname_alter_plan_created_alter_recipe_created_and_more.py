# Generated by Django 4.1.5 on 2023-02-12 10:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0006_auto_20230209_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='plan',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 12, 11, 24, 33, 974857)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 12, 11, 24, 33, 974568)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated',
            field=models.DateField(default=datetime.datetime(2023, 2, 12, 11, 24, 33, 974578)),
        ),
        migrations.CreateModel(
            name='RecipePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=128)),
                ('order', models.IntegerField(default=0)),
                ('day_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.dayname')),
                ('plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.plan')),
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='recipes',
            field=models.ManyToManyField(through='jedzonko.RecipePlan', to='jedzonko.recipe'),
        ),
    ]
