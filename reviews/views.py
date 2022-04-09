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


class SingleReview(generic.base.TemplateView):
    template_name = 'reviews/single-review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        review = models.Review.objects.get(pk=kwargs['pk'])
        context['review'] = review
        return context


# class ReviewList(generic.ListView):
#     models = models.Review
#
#     def get_queryset(self):
#         base_query = super().get_queryset()
#         data = base_query.filter(rating__gt=3)
#         return data


class SingleDetailReview(generic.DetailView):
    model = models.Review
    template_name = 'reviews/single-review.html'
