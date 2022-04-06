from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    # path('rooms/', views.RoomList.as_view(), name='rooms'),
    # path('', views.home_view, name='home'),
    path('rooms/', views.rooms_view, name='rooms'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('rooms/<room_id>/booking', views.room_booking, name='booking')
]

handler404 = "frontend.views.page_not_found_view"
