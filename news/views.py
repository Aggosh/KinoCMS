from django.shortcuts import render
from .models import New


def news(request):
    context = {"news": New.objects.all()}
    return render(request, 'news.html', context=context)


def new(request, slug):
    try:
        context = {"new": New.objects.get(slug=slug)}
    except New.DoesNotExist:
        context = {"new": []}
    return render(request, 'new.html', context=context)
