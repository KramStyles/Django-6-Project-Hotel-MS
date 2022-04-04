from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-line', 'placeholder': 'Jonathan Josiah'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-line', 'placeholder': 'Enter Password'}))
