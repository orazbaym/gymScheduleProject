from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from management.models import CustomUser

admin.site.register(CustomUser, UserAdmin)# Регистрация кастомной модели пользователя в административной панели