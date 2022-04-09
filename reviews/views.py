
from django.shortcuts import render
from django.views import View, generic

from . import models

class Review(View):
    def get(self, request):
        return render(request, 'reviews/reviews.html')


class ReviewTemplate(generic.base.TemplateView):
    template_name = 'reviews/reviews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Michael Jamie'
        context['reviews'] = models.Review.objects.all()
        return context
