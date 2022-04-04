from django.urls import path

from . import views


urlpatterns = [
    path('blank/', views.blank_view, name='dash-blank'),
    path('profile/', views.profile_view, name='dash-profile'),
]