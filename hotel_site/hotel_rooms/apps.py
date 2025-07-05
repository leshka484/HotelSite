from django.apps import AppConfig
from jobs import updater

class HotelRoomsConfig(AppConfig):
    name = "hotel_rooms"
    verbose_name = 'Номера'
    
    def ready(self) -> None:
        updater.start()
        return super().ready()

# class CategoryConfig(AppConfig):
#     name = 'category'
#     verbose_name = 'Категории'

