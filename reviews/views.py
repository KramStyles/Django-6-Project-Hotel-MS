from django.shortcuts import render
from django.views import View, generic


class Review(View):
    def get(self, request):
        return render(request, 'reviews/reviews.html')
