from django.urls import path

from . import views


urlpatterns = [
    path('dashboard/', views.blank_view, name='dash-blank'),
    path('profile/', views.profile_view, name='dash-profile'),
    path('login/', views.login_view, name='dash-login'),
    path('register/', views.register_view, name='dash-register'),
    path('admin/create/', views.create_user_view, name='dash-create-user'),
    path('admin/<int:pk>/edit', views.ProfileView.as_view(), name='dash-update-user'),
    path('admin/', views.AdminList.as_view(), name='admin-list'),
    path('admin/users', views.AllUsersList.as_view(), name='all-users'),
    path('admin/<int:pk>/delete', views.DeleteAdmin.as_view(), name='delete-admin'),
    path('logout/', views.logout_request, name='user-logout'),
    path('logs/rooms', views.RoomList.as_view(), name='room-lists'),
    path('logs/bookings', views.BookList.as_view(), name='booking-lists'),
    path('book/', views.BookingView.as_view(), name='book'),
]

