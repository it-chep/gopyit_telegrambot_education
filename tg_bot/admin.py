from django.contrib import admin
from .models import *


@admin.register(TGUsers)
class TGUsersAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'username', 'name')


@admin.register(TattooPlace)
class TattooPlace(admin.ModelAdmin):
    list_display = ('name', 'pain_level')


@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'date', 'place', 'pain_level')


@admin.register(Sketches)
class WorksAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'complexity', 'famous')


@admin.register(Dates)
class DatesAdmin(admin.ModelAdmin):
    list_display = ('date', 'status')


@admin.register(BookingTime)
class TimesAdmin(admin.ModelAdmin):
    list_display = ('time', 'expert', 'user', 'date_id')


@admin.register(TechnicalMessages)
class TechnicalMessagesAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(AllMessages)
class AllMessagesAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'date')


@admin.register(BannedUsers)
class BannedUsersAdmin(admin.ModelAdmin):
    list_display = ('user',)
