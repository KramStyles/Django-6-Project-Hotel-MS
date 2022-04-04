from django.shortcuts import render


# Create your views here.

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
    context = {
        'title': 'Login Page'
    }
    return render(request, 'dashboard/login.html', context)