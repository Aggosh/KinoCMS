from django.contrib import admin
from .models import BigPoster


@admin.register(BigPoster)
class MyAdmin(admin.ModelAdmin):
    pass
