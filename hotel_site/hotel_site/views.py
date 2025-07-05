from django.shortcuts import render


def index(request):
    return render(request, 'hotel_site/main.html', {'title': 'Главная страница'})