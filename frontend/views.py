from django.shortcuts import render
from django.views import generic


class HomeView(generic.ListView):
    model = None
    template_name = 'frontend/index.html'


def home_view(request):
    context = {
        'title': 'home'
    }
    return render(request, 'frontend/index.html', context)


def rooms_view(request):
    context = {
        'title': 'rooms'
    }
    return render(request, 'frontend/rooms.html', context)


def about_view(request):
    context = {
        'title': 'about'
    }
    return render(request, 'frontend/about.html', context)


def contact_view(request):
    context = {
        'title': 'contact'
    }
    return render(request, 'frontend/contact.html', context)

