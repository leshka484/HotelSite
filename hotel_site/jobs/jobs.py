from datetime import date


def update_reservations():
    from hotel_rooms.models import Rooms, Reservation, ReservationHistory

    # stop reservation
    reservation_end_today = Reservation.objects.filter(booked_to=date.today())
    for reservation in reservation_end_today:
        rooms_reservation_end = Rooms.objects.filter(number=reservation.room.number)
        for room in rooms_reservation_end:
            if room.is_booked:
                room.is_booked = False
                room.save()

        ReservationHistory.objects.create(
            category=reservation.category,
            booked_from=reservation.booked_from,
            booked_to=reservation.booked_to,
            user=reservation.user,
            room=reservation.room,
            guests=reservation.guests,
            price=reservation.price,
        )
        reservation.delete()

    # new reservations
    reservations_start_today = Reservation.objects.filter(booked_from=date.today())
    for reservation in reservations_start_today:
        rooms_reservation_started = Rooms.objects.filter(number=reservation.room.number)
        for room in rooms_reservation_started:
            if not room.is_booked:
                room.is_booked = True
                room.save()
    
    old_reservations = Reservation.objects.filter(booked_to__lt = date.today())
    old_reservations.delete()
