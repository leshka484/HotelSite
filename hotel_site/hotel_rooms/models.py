from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class Rooms(models.Model):
    number = models.IntegerField(verbose_name="Номер комнаты")
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, null=False, verbose_name="Категория"
    )
    is_booked = models.BooleanField(verbose_name="Забронирован ли", default=False)
    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"
        ordering = ("number",)

    def __str__(self):
        return "Номер " + str(self.number)


class Category(models.Model):
    type = models.CharField(max_length=150, verbose_name="Тип")
    beds_count = models.IntegerField(verbose_name="Количество спальных мест")
    people_count = models.IntegerField(verbose_name="Количество человек")
    # rooms_count = models.IntegerField(verbose_name='Количество комнат')
    description = models.TextField(verbose_name="Описание", default="Пустое описание")
    price = models.DecimalField(
        decimal_places=2, max_digits=10, verbose_name="Цена за ночь"
    )
    size = models.IntegerField(verbose_name="Размер комнаты")
    facilities = models.CharField(max_length=200, verbose_name="Удобства")
    mainphoto = models.ImageField(blank=True, upload_to="photos", verbose_name="Фото")

    class Meta:
        verbose_name = "Тип номера"
        verbose_name_plural = "Типы номеров"

    def get_absolute_url(self):
        return reverse("detail_room", kwargs={"category_id": self.id})

    def __str__(self):
        return self.type


class Photos(models.Model):
    category_id = models.ForeignKey(
        "Category", on_delete=models.PROTECT, null=False, verbose_name="Категория"
    )
    photo = models.ImageField(blank=True, upload_to="photos", verbose_name="Фото")

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"

    def __str__(self) -> str:
        return "Фото"


class Reservation(models.Model):
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, null=False, verbose_name="Категория"
    )
    booked_from = models.DateField(verbose_name="С")
    booked_to = models.DateField(verbose_name="До")
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Пользователь"
    )
    room = models.ForeignKey(
        "Rooms", on_delete=models.PROTECT, verbose_name="Номер комнаты"
    )
    guests = models.IntegerField(verbose_name='Количество человек')
    price = models.IntegerField(verbose_name='Цена', blank=True, default=1)

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"

    def __str__(self) -> str:
        return f"Бронирование номера {self.room} c {self.booked_from} по {self.booked_to}"

class ReservationHistory(models.Model):
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, null=False, verbose_name="Категория"
    )
    booked_from = models.DateField(verbose_name="С")
    booked_to = models.DateField(verbose_name="До")
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Пользователь"
    )
    room = models.ForeignKey(
        "Rooms", on_delete=models.PROTECT, verbose_name="Номер комнаты"
    )
    guests = models.IntegerField(verbose_name='Количество человек')
    price = models.IntegerField(verbose_name='Цена', blank=True, default=1)

    class Meta:
        verbose_name = "История бронирований"
        verbose_name_plural = "Истории бронирований"

    def __str__(self) -> str:
        return f"Бронирование номера {self.room} c {self.booked_from} по {self.booked_to}"

