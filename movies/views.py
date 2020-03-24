from django.shortcuts import render
from .models import Movie
from timetable.models import TimeTable
from django.http import Http404
import datetime
import locale


def movie(request, slug):
    try:
        movie = Movie.objects.get(slug=slug)

        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
        today = datetime.date.today()
        time_now = datetime.datetime.now().time()

        movie_timetable = []

        for time_table in TimeTable.objects.filter(date__gte=today):
            session_list = time_table.sessions.filter(movie=movie)
            if len(session_list) >= 1:
                for session in session_list:
                    if session.time > time_now:
                        movie_timetable.append(
                            {"date": time_table.date.strftime("%B %d").encode('windows-1251').decode('utf-8'),
                             "time": session.time.strftime("%H:%M"),
                             "price": session.price})
        context = {"movie": movie, "time_tables": movie_timetable}
        return render(request, 'movie.html', context=context)
    except Movie.DoesNotExist:
        raise Http404("Фильм не найден")


def movies(request):
    context = {"movies": Movie.objects.all()}
    return render(request, 'movies.html', context=context)
