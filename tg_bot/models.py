from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class TGUsers(models.Model):

    tg_id = models.IntegerField(verbose_name='id')
    username = models.CharField(max_length=255, verbose_name='Username')
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Пользователи'


class Works(models.Model):

    photo = models.ImageField(upload_to='works')
    photo_pass = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)


class NewTattoo(models.Model):

    photo_pass = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class Dates(models.Model):

    STATUS_CHOICES = (
        ('free', 'Свободный день'),
        ('partially_booked', 'Частично занят'),
        ('fully_booked', 'Полностью занят'),
        ('day_off', 'Выходной'),
    )
    date = models.DateField()
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.date)


class CustomTimeField(models.TimeField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = [(f'{hour:02d}:00', f'{hour:02d}:00') for hour in range(11, 20)]
        super().__init__(*args, **kwargs)


class BookingTime(models.Model):
    STATUS_CHOICES = (
        ('free', 'Свободное время'),
        ('booked', 'Врямя занято')
    )

    time = CustomTimeField()
    expert = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_expert',
                               limit_choices_to={'is_staff': True})
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_user')
    date_id = models.ForeignKey(Dates, on_delete=models.CASCADE)
