# Generated by Django 4.1.1 on 2023-01-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotel_rooms", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rooms",
            name="description",
        ),
        migrations.AddField(
            model_name="category",
            name="description",
            field=models.TextField(default="Пустое описание", verbose_name="Описание"),
        ),
        migrations.AddField(
            model_name="rooms",
            name="is_booked",
            field=models.BooleanField(default=False, verbose_name="Забронирован ли"),
        ),
    ]
