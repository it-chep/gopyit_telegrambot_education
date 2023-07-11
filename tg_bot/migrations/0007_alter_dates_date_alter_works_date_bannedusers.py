# Generated by Django 4.2.1 on 2023-07-10 06:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tg_bot', '0006_rename_messages_technicalmessages_alter_dates_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dates',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 10, 6, 32, 12, 17576, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='works',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 10, 6, 32, 12, 17003, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
        migrations.CreateModel(
            name='BannedUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tg_bot.tgusers')),
            ],
            options={
                'verbose_name': 'Забаненые пользователи ТГ',
                'verbose_name_plural': 'Забаненые пользователи ТГ',
            },
        ),
    ]