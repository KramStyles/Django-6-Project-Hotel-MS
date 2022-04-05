from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import LoginForm, NormalRegisterForm, AdminRegisterForm


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


def register_view(request):
    form = NormalRegisterForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            msg = 'Registration complete'
            return redirect('dash-login')
        else:
            msg = 'Form is not valid'
    context = {
        'title': 'Register',
        'form': form,
        'msg': msg
    }
    return render(request, 'dashboard/register.html', context)


def create_user_view(request):
    form = AdminRegisterForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            msg = 'Registration complete'
            return redirect('dash-profile')
        else:
            msg = 'Form is not valid'
    context = {
        'title': 'Create User',
        'form': form,
        'msg': msg
    }
    return render(request, 'dashboard/create_user.html', context)
