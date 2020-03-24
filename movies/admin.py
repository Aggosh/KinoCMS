from django.contrib import admin
from .models import Movie, Age, Country, Screenwriter, Producer, Genre, Composer, Genre, Photo


@admin.register(Movie)
class MyAdmin(admin.ModelAdmin):
    pass


@admin.register(Age)
class MyAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class MyAdmin(admin.ModelAdmin):
    pass


@admin.register(Screenwriter)
class MyAdmin(admin.ModelAdmin):
    pass


@admin.register(Producer)
class MyAdmin(admin.ModelAdmin):
    pass


@admin.register(Composer)
class MyAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class MyAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class MyAdmin(admin.ModelAdmin):
    pass
