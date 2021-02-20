import datetime
from django.shortcuts import render

from .models import HomeCaption


def home_view(request):
    current_hour = datetime.datetime.now().timetuple().tm_hour

    if request.session.get("visited", False):
        greeting_msg = "Welcome back!"
    else:
        greeting_msg = ""
        request.session["visited"] = True

    cover_caption = HomeCaption.objects.get(purpose='About the Cover')
    music_caption = HomeCaption.objects.get(purpose='About the Music')

    context = {
        'current_hour': current_hour,
        'greeting_msg': greeting_msg,
        'cover_caption': cover_caption,
        'music_caption': music_caption,
    }
    return render(request, 'home/home.html', context=context)
