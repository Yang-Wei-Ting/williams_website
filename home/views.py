import datetime
from django.shortcuts import render

from .models import HomeCaption


def home_view(request):
    current_time = datetime.datetime.now()
    current_hour = current_time.timetuple().tm_hour

    music_caption = HomeCaption.objects.get(purpose='About the Music')
    cover_caption = HomeCaption.objects.get(purpose='About the Cover')

    return render(request, 'home/home.html', locals())
