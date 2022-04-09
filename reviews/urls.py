from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewTemplate.as_view(), name='review-home'),
    path('<int:pk>/', views.SingleDetailReview.as_view(), name='review-single'),
]