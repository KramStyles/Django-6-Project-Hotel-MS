from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, RoomType, Receptionist, Payment


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-line', 'placeholder': 'Jonathan Josiah'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-line', 'placeholder': 'Enter Password'}))


class NormalRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-line', 'placeholder': 'Ifeanyi_Omaeta'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-line', 'placeholder': 'admin@hotel.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-line', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-line', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AdminRegisterForm(NormalRegisterForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-line', 'placeholder': 'Hakeem'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-line', 'placeholder': 'Rafi'}))
    is_staff = forms.RadioSelect(attrs={'class': 'form-check-input'})
    is_superadmin = forms.RadioSelect(attrs={'class': 'form-check-input'})
    is_admin = forms.RadioSelect(attrs={'class': 'form-check-input'})

    class Meta:
        model = User
        fields = ('is_admin', 'is_staff', 'is_superadmin', 'first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_admin', 'is_staff', 'is_superadmin', 'first_name', 'last_name', 'email', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-line'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-line'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-line'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control form-control-line'})
        }


class BookingForm(forms.Form):
    widget_select = forms.Select(attrs={
        'class': 'form-control',
        'style': 'max-width: 300px',
    })

    widget = forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'style': 'max-width: 300px',
    })

    widget2 = forms.DateTimeInput(attrs={
        'class': 'form-control',
        'type': 'datetime-local',
        'style': 'max-width: 300px',
    })

    # RoomTypes
    options = RoomType.objects.all()
    ROOM_TYPES = []
    for option in options:
        ROOM_TYPES.append((option.room_type, option.room_type))
    ROOM_TYPES = tuple(ROOM_TYPES)

    customers = tuple((user.id, user.username) for user in User.objects.all())
    staffs = tuple((staff.id, staff.user_id.username) for staff in Receptionist.objects.all())
    payments = tuple((payment.id, payment.amount) for payment in Payment.objects.all())

    room_type = forms.ChoiceField(widget=widget_select, choices=ROOM_TYPES, required=True)
    # customer_id = forms.IntegerField(widget=widget, required=True)
    # staff_id = forms.IntegerField(widget=widget, required=True)
    # payment_id = forms.IntegerField(widget=widget, required=True)
    staff_id = forms.ChoiceField(widget=widget_select, choices=staffs, required=True)
    payment_id = forms.ChoiceField(widget=widget_select, choices=payments, required=True)
    customer_id = forms.ChoiceField(widget=widget_select, choices=customers,required=True)
    start_date = forms.DateTimeField(widget=widget2, required=True)
    end_date = forms.DateTimeField(widget=widget2, required=True)
