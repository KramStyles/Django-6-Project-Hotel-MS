from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required

from dashboard.models import RoomType, Room
from .forms import QueryForm


class HomePage(generic.ListView):
    model = RoomType
    template_name = 'frontend/index.html'
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'home'
        context['form'] = QueryForm
        return context


# class RoomList(generic.FormView):
#     template_name = 'frontend/rooms.html'
#     model = Room
#
#     def mod_pics(self, data):
#         return (data % 7) + 1
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['title'] = 'rooms'
#         context['object_list'] = Room.objects.filter(room_status_id__status="AVAILABLE").order_by('-id')
#         context['mod'] = self.mod_pics
#         return context


def home_view(request):
    context = {
        'title': 'home',
    }
    return render(request, 'frontend/index.html', context)


def rooms_view(request):
    available_rooms = Room.objects.filter(room_status_id__status="AVAILABLE").order_by('-id')
    if request.method == 'POST':
        max_price = request.POST['max_price']
        min_price = request.POST['min_price']
        room_type = request.POST['room_type']
        # check_in = request.POST['check_in']
        # check_out = request.POST['check_out']

        if max_price:
            available_rooms = available_rooms.filter(room_type_id__price__lte=max_price)
        if min_price:
            available_rooms = available_rooms.filter(room_type_id__price__gte=min_price)
        if room_type:
            available_rooms = available_rooms.filter(room_type_id__room_type=room_type)
    else:
        form = QueryForm()
    context = {
        'title': 'rooms',
        'object_list': available_rooms,
        'rooms': RoomType.objects.all()
    }
    return render(request, 'frontend/rooms.html', context)


@login_required
def room_booking(request, room_id):
    current_room = get_object_or_404(Room, pk=room_id)
    context = {
        'room': current_room,
        'title': f'book room {room_id}'
    }
    return render(request, 'frontend/booking.html', context)


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


def page_not_found_view(request, exception):
    response = render(request, 'dashboard/pages-error-404.html', status=404)
    return response
