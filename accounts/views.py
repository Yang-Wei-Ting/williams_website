from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render


def signup_view(request):
    try:
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return HttpResponseRedirect('/accounts/login/')
    except KeyError:
        pass

    return render(request, 'registration/signup.html', locals())
