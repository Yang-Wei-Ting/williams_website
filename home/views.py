import datetime
from django.shortcuts import render

from .models import HomeCaption


def home_view(request):
    if request.session.get("visited", False):
        greeting_msg = "Welcome back!"
    else:
        greeting_msg = ""
        request.session["visited"] = True

    context = {
        'current_hour': datetime.datetime.now().timetuple().tm_hour,
        'greeting_msg': greeting_msg,
        'cover_caption': HomeCaption.objects.get(purpose='About the Cover'),
        'music_caption': HomeCaption.objects.get(purpose='About the Music'),
    }
    return render(request, 'home/home.html', context=context)
