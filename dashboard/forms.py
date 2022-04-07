from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


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
