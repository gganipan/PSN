# Generated by Django 3.0.8 on 2020-10-08 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationapp', '0025_auto_20201008_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='sensor_model',
            field=models.CharField(default='Trillium120', max_length=50, null='False'),
        ),
    ]
