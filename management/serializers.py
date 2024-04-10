from rest_framework import serializers
from .models import CustomUser, Trainer, Schedule, Booking, Gym


# Сериализатор для модели CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  # Включаем все поля модели CustomUser в сериализацию


# Сериализатор для модели Trainer
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'


# Сериализатор для модели Gym
class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'


# Сериализатор для модели Schedule
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


# Сериализатор для модели Booking
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'