from datetime import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser

DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

ROLE_CHOICES = (
        ('client', 'Client'),
        ('trainer', 'Trainer'),
        ('admin', 'Admin'),
    )


class CustomUser(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class Gym(models.Model):
    gym_name = models.CharField(max_length=100)

    def __str__(self):
        return self.gym_name


class Trainer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    gyms = models.ManyToManyField(Gym)

    def __str__(self):
        return self.full_name


class Hall(models.Model):
    name = models.CharField(max_length=100)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)


class Schedule(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, blank=True, null=True)
    day_of_week = models.CharField(max_length=20, choices=DAY_CHOICES, default='Monday')
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)


class Booking(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, blank=True, null=True)
    day_of_week = models.CharField(max_length=20, choices=DAY_CHOICES, default='Monday')
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self
