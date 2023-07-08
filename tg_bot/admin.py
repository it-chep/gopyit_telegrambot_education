from django.contrib import admin
from .models import *


@admin.register(TGUsers)
class TGUsersAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'username', 'name')


@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    list_display = ('photo', 'photo_pass', 'model_name')


@admin.register(Dates)
class DatesAdmin(admin.ModelAdmin):
    list_display = ('date', 'status')


@admin.register(BookingTime)
class TimesAdmin(admin.ModelAdmin):
    list_display = ('time', 'expert', 'user', 'date_id')

