# Generated by Django 3.0.8 on 2020-10-04 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stationapp', '0015_auto_20201004_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='save_history',
        ),
    ]