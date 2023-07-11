import os

from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

from .custom_models import CustomTimeField


class TGUsers(models.Model):
    tg_id = models.IntegerField(verbose_name='tg_id', unique=True)
    username = models.CharField(max_length=255, verbose_name='Username')
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True, unique=True)
    email = models.EmailField(blank=True)

    # blank=True - Поле необязательное

    def __str__(self):
        return f'{self.tg_id} ' + f'{self.name}'

    class Meta:
        verbose_name = 'Пользователь ТГ'
        verbose_name_plural = 'Пользователи ТГ'


class TattooPlace(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название места татуировки')
    pain_level = models.IntegerField(verbose_name='Уровень боли')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Место для татуировки'
        verbose_name_plural = 'Места для татуировок'


class Works(models.Model):
    PAIN_LEVEL_CHOICES = (
        ('1', 'Низкий уровень боли'),
        ('2', 'Средний уровень боли'),
        ('3', 'Высокий уровень боли'),
    )

    name = models.CharField(max_length=255, verbose_name='Название татуировки')
    photo = models.ImageField(upload_to='works', verbose_name='Фотография')
    date = models.DateField(default=timezone.now(), verbose_name='Дата')
    place = models.OneToOneField(to=TattooPlace, on_delete=models.PROTECT, default=1, verbose_name='Место татуировки')
    pain_level = models.CharField(max_length=40, choices=PAIN_LEVEL_CHOICES, default=1, verbose_name='Уровень боли')

    # category = ...

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Моя работа'
        verbose_name_plural = 'Мои работы'


class Sketches(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    photo = models.ImageField(verbose_name='Фотография', upload_to='sketches')
    # category = ...
    complexity = models.IntegerField(verbose_name='Сложность эскиза', default=0)
    famous = models.IntegerField(verbose_name='Популярность эскиза', default=0)

    class Meta:
        verbose_name = 'Эскиз'
        verbose_name_plural = 'Эскизы'


class Dates(models.Model):
    STATUS_CHOICES = (
        ('free', 'Свободный день'),
        ('partially_booked', 'Частично занят'),
        ('fully_booked', 'Полностью занят'),
        ('day_off', 'Выходной'),
    )
    date = models.DateField(verbose_name='Дата', default=timezone.now())
    status = models.CharField(verbose_name='Статус дня', max_length=40, choices=STATUS_CHOICES, default='free')

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Дата бесплатной консультации'
        verbose_name_plural = 'Даты бесплатных консультаций'


class BookingTime(models.Model):
    STATUS_CHOICES = (
        ('free', 'Свободное время'),
        ('booked', 'Врямя занято')
    )

    time = CustomTimeField()
    expert = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_expert',
                               limit_choices_to={'is_staff': True})
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_user', blank=True)
    date_id = models.ForeignKey(Dates, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Время консультаций'
        verbose_name_plural = 'Время консультаций'


class TechnicalMessages(models.Model):
    name = models.CharField(verbose_name='Название сообщения', max_length=255)
    text = models.TextField(blank=True)
    sticker_id = models.CharField(blank=True, max_length=255, verbose_name='Любимый Стикер')

    class Meta:
        verbose_name = 'Текстовые сообщения в бота'
        verbose_name_plural = 'Текстовые сообщения в бота'


class Feedback(models.Model):
    name = models.CharField(verbose_name='Имя пользователя')
    user_name = models.CharField(verbose_name='Ссылка на пользователя', default='')
    photo = models.ImageField(verbose_name='Фото отзыв', blank=True, upload_to='feedbacks')
    photo_pass = models.CharField(verbose_name='Cсыдка на источник с фото', blank=True)
    video_link = models.CharField(verbose_name='Видео отзы', blank=True)
    text = models.TextField(verbose_name='Текст отзыва')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class FavouriteStickers(models.Model):
    sticker_id = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Стикер'
        verbose_name_plural = 'Стикеры'


class AllMessages(models.Model):
    user = models.ForeignKey(TGUsers, models.CASCADE)
    text = models.TextField(verbose_name='Текс сообщения')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время сообщения')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Все сообщения'


class BannedUsers(models.Model):
    user = models.OneToOneField(TGUsers, models.CASCADE)

    class Meta:
        verbose_name = 'Забаненые пользователи ТГ'
        verbose_name_plural = 'Забаненые пользователи ТГ'

