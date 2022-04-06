from django.urls import path

from . import views


urlpatterns = [
    path('blank/', views.blank_view, name='dash-blank'),
    path('profile/', views.profile_view, name='dash-profile'),
    path('login/', views.login_view, name='dash-login'),
    path('register/', views.register_view, name='dash-register'),
    path('create_user/', views.create_user_view, name='dash-create-user'),
    path('profile/update/<int:pk>/', views.ProfileView.as_view(), name='dash-update-user')
]

