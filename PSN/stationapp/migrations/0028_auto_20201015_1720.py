# Generated by Django 3.0.8 on 2020-10-15 17:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stationapp', '0027_auto_20201014_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='installation_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='station',
            name='sensor_start_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='station',
            name='transceiver_sn',
            field=models.CharField(default='0000', max_length=50, null='False'),
            preserve_default='False',
        ),
    ]
