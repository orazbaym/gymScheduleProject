from datetime import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser

# Определяем выбор дней недели для использования в моделях
DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

# Определяем выбор ролей пользователей
ROLE_CHOICES = (
        ('client', 'Client'),
        ('trainer', 'Trainer'),
        ('admin', 'Admin'),
    )


# Создаем кастомную модель пользователя AbstractUser
class CustomUser(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


# Модель зала
class Gym(models.Model):
    gym_name = models.CharField(max_length=100)

    def __str__(self):
        return self.gym_name


# Модель тренера
class Trainer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # Связываем с кастомной моделью пользователя
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    gyms = models.ManyToManyField(Gym)  # Связь с залами, в которых работает тренер

    def __str__(self):
        return self.full_name


# Модель расписания
class Schedule(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(max_length=10, blank=True, null=True)  # Дата расписания
    day_of_week = models.CharField(max_length=20, choices=DAY_CHOICES, default='Monday')  # День недели
    start_time = models.TimeField(blank=True, null=True)  # Время начала работы
    end_time = models.TimeField(blank=True, null=True)  # Время окончания работы


# Модель записи
class Booking(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Клиент, записавшийся на тренировку
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)  # Тренер, к которому записались
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, blank=True, null=True)  # Зал, в котором будет тренировка
    day_of_week = models.CharField(max_length=20, choices=DAY_CHOICES, default='Monday')  # День недели
    start_time = models.TimeField(blank=True, null=True)  # Время начала тренировки
    end_time = models.TimeField(blank=True, null=True)  # Время окончания тренировки
