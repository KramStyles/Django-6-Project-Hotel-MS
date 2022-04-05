from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('', views.home_view, name='home'),
    path('rooms/', views.rooms_view, name='rooms'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]