from django.db import models


class Movie(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        verbose_name='Название фильма')
    premiere_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Дата примьеры")
    poster = models.ImageField(
        upload_to='img/posters',
        verbose_name="Постер")
    slug = models.SlugField(
        verbose_name='URL',
        max_length=50,
        unique=True,)

    def __str__(self):
        return(f'{self.title}')
