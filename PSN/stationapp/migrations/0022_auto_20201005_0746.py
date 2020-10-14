# Generated by Django 3.0.8 on 2020-10-05 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationapp', '0021_repair_station_type_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='station_type_field',
            field=models.CharField(choices=[('ST', 'STSS'), ('MO', 'Main Office')], default='MO', max_length=2),
        ),
    ]
