# Generated by Django 3.0.8 on 2020-10-04 12:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stationapp', '0009_auto_20201004_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='repair_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 10, 4, 12, 12, 37, 431448, tzinfo=utc)),
        ),
    ]
