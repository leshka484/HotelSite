from typing import Any, Mapping, Optional, Type, Union
from django.forms import (
    DateField,
    DateInput,
    ModelChoiceField,
    Select,
    TextInput,
    ValidationError,
    Form,
    CharField,
    IntegerField,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.utils import ErrorList
from .models import Category, Rooms, Reservation
from django.db.models import Q
import re


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Эта почта уже зарегистрирована")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        print(first_name)
        if not re.fullmatch(r'^([А-Я]{1}[а-яё]{1,23})$', first_name):
            raise ValidationError('Имя должно быть написано кириллицей с большой буквы')
        
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not re.fullmatch(r'^([А-Я]{1}[а-яё]{1,23})$',last_name):
            raise ValidationError('Фамилия должна быть написана кириллицей с большой буквы')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        #fields = ["username", "email", "password1", "password2"]


class BookingForm(Form):
    room_type = ModelChoiceField(
        label="Номер",
        queryset=Category.objects.all(),
        empty_label="Категория не выбрана",
        widget=Select(attrs={"class": "form-group"}),
    )
    entrance = DateField(
        label="Дата въезда",
        widget=DateInput(attrs={"type": "date", "class": "date-in"}, format="%Y-%m-%d"),
    )
    check_out = DateField(
        label="Дата выезда",
        widget=DateInput(
            attrs={"type": "date", "class": "date-out"}, format="%Y-%m-%d"
        ),
    )
    guests = IntegerField(label="Количество гостей", min_value=1, max_value=4)

    # def clean_room_type(self):
    #     cleaned_data = super().clean()
    #     room_type = cleaned_data.get("room_type")
    #     room = Rooms.objects.filter(
    #         Q(category__type__icontains=room_type) & Q(is_booked=False)
    #     ).first()

    #     if room is None:
    #         raise ValidationError(
    #             "Сейчас невозможно подобрать такой номер. Выберите другой."
    #         )

    def clean(self):
        cleaned_data = super().clean()
        room_type = cleaned_data.get("room_type")
        entrance = cleaned_data.get("entrance")
        check_out = cleaned_data.get("check_out")
        rooms = Rooms.objects.filter(Q(category__type=room_type))
        for room in rooms:
            reservations = Reservation.objects.filter(Q(room__number=room.number))
            if not reservations:
                return 
            for reservation in reservations:
                if (
                        entrance >= reservation.booked_from
                        and entrance < reservation.booked_to
                    or (
                        entrance < reservation.booked_from
                        and check_out > reservation.booked_to
                    )
                    or (
                        check_out > reservation.booked_from
                        and check_out < reservation.booked_to
                    )
                ):
                    break
                return
        raise ValidationError("Вы не можете забронировать этот номер на эти даты")