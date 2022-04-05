from django.shortcuts import render
from django.views import generic

from dashboard.models import RoomType, Room


class HomePage(generic.ListView):
    model = RoomType
    template_name = 'frontend/index.html'
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'home'
        return context


class RoomList(generic.TemplateView):
    template_name = 'frontend/rooms.html'

    def mod_pics(self, data):
        return (data % 7) + 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'rooms'
        context['object_list'] = Room.objects.filter(room_status_id__status="AVAILABLE").order_by('-id')
        context['mod'] = self.mod_pics
        return context


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
