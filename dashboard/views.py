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
