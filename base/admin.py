from django.contrib import admin
from .models import BigPoster
from django.contrib.auth.models import Group


class BigPosterAdmin(admin.ModelAdmin):
    pass


admin.site.register(BigPoster)
admin.site.unregister(Group)
