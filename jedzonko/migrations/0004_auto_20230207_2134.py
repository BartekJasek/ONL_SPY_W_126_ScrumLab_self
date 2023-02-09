# Generated by Django 2.2.6 on 2023-02-07 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0003_alter_recipe_created_alter_recipe_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('created', models.DateField(default=datetime.datetime(2023, 2, 7, 21, 34, 50, 822290))),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 21, 34, 50, 822022)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated',
            field=models.DateField(default=datetime.datetime(2023, 2, 7, 21, 34, 50, 822033)),
        ),
    ]