from django.db import models
from movies.models import Movie


class Session(models.Model):
    time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Сеанс")

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        verbose_name="Фильм")

    price = models.FloatField(
        default=50.00,
        verbose_name="Цена")

    def __str__(self):
        time = self.time.strftime('%H:%M')
        return f'{time} {self.movie} {self.price}грн'


class TimeTable(models.Model):
    date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Дата")

    sessions = models.ManyToManyField(
        Session,
        verbose_name="Сеансы")

    def __str__(self):
        return str(self.date)
