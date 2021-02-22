from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SignupForm


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', context={'form': form})
