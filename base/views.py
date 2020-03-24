from django.shortcuts import render
from movies.models import Movie
from timetable.models import TimeTable
from .models import BigPoster
import datetime
import locale


def index(request):
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    today = datetime.date.today()

    try:
        today_movies = []
        today_table = TimeTable.objects.get(date=today)
        for session in today_table.sessions.all():
            today_movies.append(session.movie)

        today_movies = list(set(today_movies))
    except TimeTable.DoesNotExist:
        today_movies = []

    context = {"today_movies": today_movies,
               "after_movies": Movie.objects.filter(premiere_date__gt=today),
               "today_date": today.strftime("%B %d").encode('windows-1251').decode('utf-8'),
               "big_posters": BigPoster.objects.all()}
    return render(request, 'index.html', context=context)
