# Generated by Django 3.0.8 on 2020-10-15 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stationapp', '0028_auto_20201015_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='sensor_start_date',
            new_name='battery_start_date',
        ),
    ]
