from django.db import models


class New(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название")
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата")
    description = models.TextField(
        max_length=10000,
        verbose_name="Описание")
    photo = models.ImageField(
        upload_to="img/news",
        verbose_name="Фото")
    slug = models.SlugField(
        max_length=255,
        verbose_name="URL")

    def __str__(self):
        return self.title
