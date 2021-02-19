import datetime
from django.shortcuts import render

from .models import HomeCaption


def home_view(request):
    music_caption = HomeCaption.objects.get(purpose='About the Music')
    cover_caption = HomeCaption.objects.get(purpose='About the Cover')

    current_hour = datetime.datetime.now().timetuple().tm_hour

    return render(request, 'home/home.html', locals())
