# Generated by Django 3.2.19 on 2023-06-21 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('life_saver_user_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='life_saver_user_auth.user')),
                ('blood_group', models.CharField(max_length=30)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('age', models.IntegerField()),
                ('is_profile_complete', models.BooleanField(default=False)),
            ],
        ),
    ]
