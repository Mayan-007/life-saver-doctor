# Generated by Django 3.2.19 on 2023-06-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life_saver_appointment', '0005_appointment_doctor_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patient_remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
