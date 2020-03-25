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
                    if time_table.date == today:
                        if session.time > time_now:
                            movie_timetable.append(
                                {"date": time_table.date.strftime("%B %d").encode('windows-1251').decode('utf-8'),
                                 "time": session.time.strftime("%H:%M"),
                                 "price": session.price})
                    else:
                        movie_timetable.append(
                            {"date": time_table.date.strftime("%B %d").encode('windows-1251').decode('utf-8'),
                             "time": session.time.strftime("%H:%M"),
                             "price": session.price})
        context = {"movie": movie, "time_tables": movie_timetable}
        return render(request, 'movie.html', context=context)
    except Movie.DoesNotExist:
        raise Http404("Фильм не найден")


def movies(request):
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    today = datetime.date.today()

    try:
        rental_movies = []
        rental_tables = TimeTable.objects.filter(date__gte=today)
        for rental in rental_tables:
            for movie in rental.sessions.all():
                rental_movies.append(movie.movie)
        rental_movies = list(set(rental_movies))
    except TimeTable.DoesNotExist:
        rental_movies = []

    context = {"rental_movies": rental_movies,
               "soon_rental_movies": Movie.objects.filter(premiere_date__gt=today)}
    return render(request, 'movies.html', context=context)
