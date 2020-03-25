from django.shortcuts import render
from movies.models import Movie


def poster(request):
    context = {"movies": Movie.objects.all()}
    return render(request, 'poster.html', context=context)