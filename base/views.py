from django.shortcuts import render
from movies.models import Movie
import datetime
import locale


def index(request):
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    today = datetime.date.today()
    context = {"today_movies": Movie.objects.filter(premiere_date__lte=today),
               "after_movies": Movie.objects.filter(premiere_date__gt=today),
               "today_date": today.strftime("%B %d").encode('windows-1251').decode('utf-8')}
    return render(request, 'index.html', context=context)
