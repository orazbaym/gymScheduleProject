from rest_framework import generics
from .models import CustomUser, Trainer, Schedule, Booking, Gym
from .serializers import CustomUserSerializer, TrainerSerializer, ScheduleSerializer, BookingSerializer, GymSerializer


class CustomUserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class TrainerListCreate(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class GymListCreate(generics.ListCreateAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


class ScheduleListCreate(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class BookingListCreate(generics.ListCreateAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.all()
        gym_id = self.request.query_params.get('gym_id')
        hall_id = self.request.query_params.get('hall_id')
        day_of_week = self.request.query_params.get('day_of_week')

        if gym_id and hall_id and day_of_week:
            queryset = queryset.filter(hall__gym_id=gym_id, hall_id=hall_id, day_of_week=day_of_week)

        return queryset

    def perform_create(self, serializer):
        gym_id = self.request.data.get('gym_id')
        hall_id = self.request.data.get('hall_id')
        trainer_id = self.request.data.get('trainer_id')
        day_of_week = self.request.data.get('day_of_week')
        # Here you can perform additional validation or logic before saving the booking
        serializer.save(gym_id=gym_id, hall_id=hall_id, trainer_id=trainer_id, day_of_week=day_of_week)
