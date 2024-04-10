# Generated by Django 5.0.4 on 2024-04-10 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_remove_booking_gym_remove_schedule_gym_trainer_gyms_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='hall',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='hall',
        ),
        migrations.AddField(
            model_name='booking',
            name='gym',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.gym'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.DateField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='gym',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.gym'),
        ),
        migrations.DeleteModel(
            name='Hall',
        ),
    ]
