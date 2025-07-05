from django.contrib import admin
from .models import Rooms, Category, Photos, Reservation, ReservationHistory

# Register your models here.


class RoomsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "number",
        "category",
        "is_booked",
    )
    list_display_links = (
        "id",
        "number",
    )
    search_fields = (
        "number",
        "category",
    )
    list_filter = (
        "is_booked",
        "category",
    )
    list_editable = ("is_booked",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "type",
        "beds_count",
        "people_count",
        "description",
        "price",
        "size",
        "facilities",
    )
    list_display_links = (
        "id",
        "type",
    )
    search_fields = (
        "type",
        "beds_count",
        "people_count",
        "price",
        "size",
    )
    list_filter = (
        "beds_count",
        "people_count",
    )


class PhotosAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category_id",
        "photo",
    )
    list_display_links = (
        "id",
        "category_id",
    )
    search_fields = ("category_id",)
    list_filter = ("category_id",)


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "booked_from",
        "booked_to",
        "user",
        "room",
        "guests",
        "price",
    )
    list_display_links = ("id",)
    search_fields = (
        "booked_from",
        "booked_to",
        "user",
        "room",
        "guests",
        "price",
    )
    list_filter = (
        "booked_from",
        "booked_to",
        "user",
        "room",
        "guests",
    )

class ReservationHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "booked_from",
        "booked_to",
        "user",
        "room",
        "guests",
        "price",
    )
    list_display_links = ("id",)
    search_fields = (
        "booked_from",
        "booked_to",
        "user",
        "room",
        "guests",
        "price",
    )
    list_filter = (
        "booked_from",
        "booked_to",
        "user",
        "room",
        "guests",
    )

admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Photos, PhotosAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservationHistory, ReservationHistoryAdmin)
admin.site.site_title = "Панель администратора"
admin.site.site_header = "Администрирование гостиницы"

