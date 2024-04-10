from django.contrib import admin
from django.urls import path

from management.views import *

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для доступа к административной панели Django
    path('users/', CustomUserListCreate.as_view(), name='user-list'),  # URL для работы с пользователями
    path('trainers/', TrainerListCreate.as_view(), name='trainer-list'),  # URL для работы с тренерами
    path('gyms/', GymListCreate.as_view(), name='gym-list'),  # URL для работы с залами
    path('schedules/', ScheduleListCreate.as_view(), name='schedule-list'),  # URL для работы с расписаниями
    path('bookings/', BookingListCreate.as_view(), name='booking-list'),  # URL для работы с записями
]
