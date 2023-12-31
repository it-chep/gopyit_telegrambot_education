# Generated by Django 4.2.1 on 2023-07-09 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_bot', '0004_messages_alter_dates_date_alter_works_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteStickers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sticker_id', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Стикер',
                'verbose_name_plural': 'Стикеры',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Имя пользователя')),
                ('user_name', models.CharField(default='', verbose_name='Ссылка на пользователя')),
                ('photo', models.ImageField(blank=True, upload_to='feedbacks', verbose_name='Фото отзыв')),
                ('photo_pass', models.CharField(blank=True, verbose_name='Cсыдка на источник с фото')),
                ('video_link', models.CharField(blank=True, verbose_name='Видео отзы')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='messages',
            name='sticker_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='Любимый Стикер'),
        ),
        migrations.AlterField(
            model_name='dates',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 22, 49, 20, 107627, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='works',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 22, 49, 20, 106946, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
    ]
