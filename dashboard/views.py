from django.shortcuts import render


# Create your views here.

def blank_view(request):
    context = {
        'title': 'Blank Page'
    }
    return render(request, 'dashboard/blank.html', context)
