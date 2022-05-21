import datetime

from django.shortcuts import render


def home_view(request):
    if "visited" in request.session and request.session["visited"] is True:
        greeting_msg = "Welcome Back!"
    else:
        greeting_msg = ""
        request.session["visited"] = True

    context = {
        'current_hour': datetime.datetime.now().timetuple().tm_hour,
        'greeting_msg': greeting_msg,
    }
    return render(request, 'home/home.html', context=context)


def page_not_found_view(request, exception):
    context = {'current_hour': datetime.datetime.now().timetuple().tm_hour}
    return render(request, 'home/page_not_found.html', context=context, status=404)
