# Generated by Django 5.0.4 on 2024-04-09 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_gym_remove_booking_schedule_booking_day_of_week_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='gym',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='gym',
        ),
        migrations.AddField(
            model_name='trainer',
            name='gyms',
            field=models.ManyToManyField(to='management.gym'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='day_of_week',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=20),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='day_of_week',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=20),
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.gym')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='hall',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.hall'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='hall',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.hall'),
        ),
    ]
