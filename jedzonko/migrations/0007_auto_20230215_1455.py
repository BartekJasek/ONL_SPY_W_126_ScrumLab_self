# Generated by Django 2.2.6 on 2023-02-15 13:55

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
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 14, 55, 40, 434750)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 14, 55, 40, 434403)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 14, 55, 40, 434421)),
        ),
        migrations.CreateModel(
            name='RecipePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=128)),
                ('order', models.IntegerField(default=0)),
                ('day_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.DayName')),
                ('plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.Plan')),
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='recipes',
            field=models.ManyToManyField(through='jedzonko.RecipePlan', to='jedzonko.Recipe'),
        ),
    ]
