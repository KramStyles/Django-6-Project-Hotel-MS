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


def home_view_2(request):
    context = {
        'title': 'home'
    }
    return render(request, 'frontend/index-2.html', context)
