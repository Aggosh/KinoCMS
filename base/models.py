from django.db import models


class BigPoster (models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название')
    poster = models.ImageField(
        upload_to='img/big_posters')

    def __str__(self):
        return self.title
