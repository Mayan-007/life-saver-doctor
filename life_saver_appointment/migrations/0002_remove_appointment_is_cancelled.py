# Generated by Django 3.2.19 on 2023-06-22 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('life_saver_appointment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='is_cancelled',
        ),
    ]