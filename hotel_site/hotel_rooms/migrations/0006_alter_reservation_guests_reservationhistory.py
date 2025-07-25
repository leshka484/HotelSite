# Generated by Django 4.1.1 on 2023-05-22 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_rooms', '0005_alter_category_mainphoto_alter_photos_category_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guests',
            field=models.IntegerField(verbose_name='Количество человек'),
        ),
        migrations.CreateModel(
            name='ReservationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_from', models.DateField(verbose_name='С')),
                ('booked_to', models.DateField(verbose_name='До')),
                ('guests', models.IntegerField(verbose_name='Количество человек')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_rooms.category', verbose_name='Категория')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_rooms.rooms', verbose_name='Номер комнаты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'История бронирований',
                'verbose_name_plural': 'Истории бронирований',
            },
        ),
    ]
