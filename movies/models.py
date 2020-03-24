from django.db import models


class Country(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название страны')

    slug = models.SlugField(
        max_length=100,
        verbose_name="URL")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Screenwriter(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя сценариста')

    slug = models.SlugField(
        max_length=100,
        verbose_name="URL")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя продюсера')

    slug = models.SlugField(
        max_length=100,
        verbose_name="URL")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название жанра')

    slug = models.SlugField(
        max_length=100,
        verbose_name="URL")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Composer(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя композитора')

    slug = models.SlugField(
        max_length=100,
        verbose_name="URL")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Age(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Возраст')

    slug = models.SlugField(
        max_length=100,
        verbose_name="URL")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название кадра")
    photo = models.ImageField(
        upload_to='img/frames',
        verbose_name='Кадр из фильма')

    class Meta:
        ordering = ['photo']

    def __str__(self):
        return self.title


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
    youtube = models.CharField(
        max_length=50,
        verbose_name="Адреес youtube трейлера")

    countrys = models.ManyToManyField(
        Country,
        verbose_name="Страны")
    screenwriters = models.ManyToManyField(
        Screenwriter,
        verbose_name="Сценаристы")
    producers = models.ManyToManyField(
        Producer,
        verbose_name="Продюсеры")
    genres = models.ManyToManyField(
        Genre,
        verbose_name="Жанры")
    composers = models.ManyToManyField(
        Composer,
        verbose_name="Компазиторы")
    age = models.ForeignKey(
        Age,
        on_delete=models.CASCADE,
        verbose_name="Возраст")

    budget = models.CharField(
        max_length=100,
        verbose_name="Бюджет")
    time = models.CharField(
        max_length=100,
        verbose_name="Время")
    slug = models.SlugField(
        verbose_name='URL',
        max_length=50,
        unique=True)

    description = models.TextField(
        max_length=255,
        verbose_name="Описание")

    photos = models.ManyToManyField(
        Photo,
        verbose_name="Кадры фильма")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return(f'{self.title}')
