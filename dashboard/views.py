from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import LoginForm


def blank_view(request):
    context = {
        'title': 'Blank Page'
    }
    return render(request, 'dashboard/blank.html', context)


def profile_view(request):
    context = {
        'title': 'Profile Page'
    }
    return render(request, 'dashboard/profile.html', context)


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dash-profile')
            else:
                msg = 'Incorrect Credentials'
        else:
            msg = 'Check your Inputs'
    context = {
        'title': 'Login Page',
        'form': form,
        'msg': msg
    }
    return render(request, 'dashboard/login.html', context)
