# Generated by Django 3.0.8 on 2020-10-04 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stationapp', '0017_history_save_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='save_history',
        ),
    ]