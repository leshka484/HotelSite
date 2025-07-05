from datetime import datetime, date
from typing import Any, Dict, Optional, Type
from django.db.models.query import QuerySet
from django.forms.forms import BaseForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView, DetailView, CreateView, FormView
from .forms import BookingForm, UserRegisterForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.db.models import Q
from jobs.jobs import update_reservations
import re

# Create your views here.


class ShowRooms(ListView):
    model = Category
    template_name = "hotel_rooms/rooms.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(self.request.GET.dict())
        # context["extramessage"] = "Выберите номер себе по вкусу"
        context["title"] = "Номера"
        # context["categories"] = Category.objects.all()
        return context

    def get_queryset(self) -> QuerySet[Any]:
        try:
            booked_from = datetime.strptime(
                self.request.GET.get("check-in"), "%Y-%m-%d"
            ).date()
        except:
            booked_from = None
        try:
            booked_to = datetime.strptime(
                self.request.GET.get("check-out"), "%Y-%m-%d"
            ).date()
        except:
            booked_to = None
        guests = self.request.GET.get("guest")

        if not booked_from and not booked_to and not guests:
            return Category.objects.all()

        if booked_from and booked_to and guests:
            showed_categories = []
            categories = Category.objects.filter(
                Q(people_count__gte=int(guests) - 1)
                & Q(people_count__lte=int(guests) + 1)
            )
            for category in categories:
                category_rooms = Rooms.objects.filter(category__type=category)
                for room in category_rooms:
                    reservations = Reservation.objects.filter(room__number=room.number)
                    if not reservations:
                        showed_categories.append(category)
                        break
                    for reservation in reservations:
                        if (
                            booked_from >= reservation.booked_from
                            and booked_from < reservation.booked_to
                            or (
                                booked_from < reservation.booked_from
                                and booked_to > reservation.booked_to
                            )
                            or (
                                booked_to > reservation.booked_from
                                and booked_to < reservation.booked_to
                            )
                        ):
                            break
                        showed_categories.append(category)
            return Category.objects.filter(type__in=showed_categories)

        if (not booked_from or not booked_to) and guests:
            return Category.objects.filter(
                Q(people_count__gte=int(guests) - 1)
                & Q(people_count__lte=int(guests) + 1)
            )

        if booked_from and booked_to and not guests:
            showed_categories = []
            categories = Category.objects.all()
            for category in categories:
                category_rooms = Rooms.objects.filter(category__type=category)
                for room in category_rooms:
                    reservations = Reservation.objects.filter(room__number=room.number)
                    if not reservations:
                        showed_categories.append(category)
                        break
                    for reservation in reservations:
                        if (
                            booked_from >= reservation.booked_from
                            and booked_from < reservation.booked_to
                            or (
                                booked_from < reservation.booked_from
                                and booked_to > reservation.booked_to
                            )
                            or (
                                booked_to > reservation.booked_from
                                and booked_to < reservation.booked_to
                            )
                        ):
                            break
                        showed_categories.append(category)
            return Category.objects.filter(type__in=showed_categories)


class RoomsFilter(ListView):
    model = Rooms
    template_name = "hotel_rooms/rooms.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Номера"
        return context

    def get_queryset(self) -> QuerySet[Any]:
        guests = self.request.GET.get("guest")
        str_price = self.request.GET.get("price")
        prices = re.findall(r"\d{3}", str_price)
        price_from = int(prices[0])
        price_to = int(prices[1])
        return Category.objects.filter(
            Q(people_count=guests) & Q(price__gte=price_from) & Q(price__lte=price_to)
        )


class ShowDetails(DetailView):
    model = Category
    template_name = "hotel_rooms/room_details.html"
    pk_url_kwarg = "category_id"
    context_object_name = "room"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Номера"
        # context['photos'] = Photos.objects.filter(category_id = self.object.pk).select_related("category_id")
        if "category_id" in self.kwargs:
            context["category_id"] = self.kwargs["category_id"]
        context["photos"] = Photos.objects.filter(category_id=self.object.pk)
        return context


def show_contacts(request):
    return render(request, "hotel_rooms/contact.html", {"title": "Контакты"})


def show_about(request):
    return render(request, "hotel_rooms/about.html", {"title": "О Нас"})


class Register(CreateView):
    form_class = UserRegisterForm
    template_name = "hotel_rooms/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class Login(LoginView):
    form_class = UserLoginForm
    template_name = "hotel_rooms/login.html"

    def get_success_url(self):
        return reverse_lazy("home")


def logout_user(request):
    logout(request)
    return redirect("login")


class Booking(FormView):
    form_class = BookingForm
    template_name = "hotel_rooms/reservation.html"
    success_url = reverse_lazy("rooms")

    def get_initial(self) -> Dict[str, Any]:
        initial = super().get_initial()
        #print(self.request.GET.dict())
        category = Category.objects.get(pk=self.request.GET["category_id"])
        initial["room_type"] = category
        if self.request.GET["in"]:
            initial["entrance"] = datetime.strptime(self.request.GET["in"], "%Y-%m-%d")
        if self.request.GET["out"]:
            initial["check_out"] = datetime.strptime(
                self.request.GET["out"], "%Y-%m-%d"
            )
        if self.request.GET["guest"]:
            initial["guests"] = int(self.request.GET["guest"])
        return initial

    def form_valid(self, form: Any) -> HttpResponse:
        print(form.cleaned_data)
        print(form["room_type"].value())
        category = form.cleaned_data["room_type"]
        booked_from = form.cleaned_data["entrance"]
        booked_to = form.cleaned_data["check_out"]
        guests = form.cleaned_data["guests"]
        user = self.request.user
        ###########################
        rooms = Rooms.objects.filter(Q(category__type=category))
        for room in rooms:
            reservations = Reservation.objects.filter(Q(room__number=room.number))
            if not reservations:
                room_for_reservation = room
                break
            for reservation in reservations:
                if (
                    booked_from >= reservation.booked_from
                    and booked_from < reservation.booked_to
                    or (
                        booked_from < reservation.booked_from
                        and booked_to > reservation.booked_to
                    )
                    or (
                        booked_to > reservation.booked_from
                        and booked_to < reservation.booked_to
                    )
                ):
                    break
                room_for_reservation = room
        ###########################
        Reservation.objects.create(
            category=category,
            booked_from=booked_from,
            booked_to=booked_to,
            guests=guests,
            user=user,
            room=room_for_reservation,
        )
        update_reservations()
        return redirect("home")

class CurrentReservations(ListView):
    model = Reservation
    template_name = "hotel_rooms/current_reservations.html"
    context_object_name = "reservations"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Брони"
        reservations = Reservation.objects.filter(Q(booked_to__gte = date.today()) & Q(user = self.request.user))
        context['reservations'] = reservations
        return context


class HistoryReservations(ListView):
    model = ReservationHistory
    template_name = "hotel_rooms/history_reservations.html"
    context_object_name = "reservations"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "История бронирований"
        reservations = ReservationHistory.objects.filter(Q(booked_to__lte = date.today()) & Q(user = self.request.user))
        context['reservations'] = reservations
        return context