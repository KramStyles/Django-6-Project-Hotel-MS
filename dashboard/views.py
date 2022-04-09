from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from .forms import LoginForm, NormalRegisterForm, AdminRegisterForm, UserUpdateForm, BookingForm
from .models import User, Room, Booking, Reservation, Receptionist, Payment


def blank_view(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/blank.html', context)


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
            msg = form.errors
    context = {
        'title': 'Create User',
        'form': form,
        'msg': msg
    }
    return render(request, 'dashboard/create_user.html', context)


@login_required
def profile_view(request):
    msg = None
    context = {
        'title': 'Profile Page',
        'msg': msg
    }
    return render(request, 'dashboard/profile.html', context)


def logout_request(request):
    logout(request)
    return redirect('dash-login')


class ProfileView(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = 'dashboard/update_profile.html'
    form_class = UserUpdateForm

    success_url = '/profile'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        context['title'] = 'Update Profile'
        context['author'] = self.request.user
        return context


class AdminList(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'dashboard/admin_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['admins'] = self.model.objects.exclude(is_superuser=True).exclude(is_staff=False, is_admin=False, is_superadmin=False)
        context['title'] = 'Admin List'
        return context


class AllUsersList(AdminList):
    template_name = 'dashboard/all_users.html'

    def get_context_data(self, **kwargs):
        context = super(AllUsersList, self).get_context_data()
        context['users'] = self.model.objects.exclude(is_superuser=True)
        context['title'] = 'All Users'
        return context


class DeleteAdmin(LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = '/admin'
    template_name = 'dashboard/delete_admin.html'

    def get_context_data(self, **kwargs):
        context = super(DeleteAdmin, self).get_context_data()
        context['title'] = 'Delete Manager'
        return context


class RoomList(LoginRequiredMixin, generic.ListView):
    model = Room
    template_name = 'dashboard/logs/rooms.html'
    context_object_name = 'rooms'


class BookList(LoginRequiredMixin, generic.ListView):
    model = Booking
    template_name = 'dashboard/logs/bookings.html'
    context_object_name = 'bookings'


class BookingView(LoginRequiredMixin, generic.FormView):
    form_class = BookingForm
    template_name = 'dashboard/booking.html'

    def validation(self, room, start_date, end_date):
        check = []
        booking_list = Reservation.objects.filter(room_id=room)
        for booking in booking_list:
            if booking.start_time > end_date or booking.end_time < start_date:
                check.append(True)
            else:
                check.append(False)
        return all(check)

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(room_type_id__room_type=data['room_type'])
        if available_rooms := [room for room in room_list if self.validation(room, data['start_date'], data['end_date'])]:
            booking = Booking.objects.create(
                room_id=available_rooms[0],
                customer_id=User.objects.get(pk=data['customer_id']),
                staff_id=Receptionist.objects.get(pk=data['staff_id']),
                payment_id=Payment.objects.get(pk=data['payment_id']),
            )
            booking.save()
            return redirect('booking-lists')
        else:
            return HttpResponse("All the rooms are booked for the room type!")
