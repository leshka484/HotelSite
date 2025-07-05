from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path("rooms/", ShowRooms.as_view(), name = 'rooms'),
    path("rooms_filtered/", RoomsFilter.as_view(), name = 'rooms_filtered'),
    path("contacts/", views.show_contacts, name = 'contacts'),
    path("about/", views.show_about, name = 'about'),
    path('rooms/<int:category_id>/', ShowDetails.as_view(), name = 'detail_room'),
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('booking', Booking.as_view(), name = 'booking'),
    path('current_reservations', CurrentReservations.as_view(), name = 'current_reservations'),
    path('history_reservations', HistoryReservations.as_view(), name = 'history_reservations'),
]