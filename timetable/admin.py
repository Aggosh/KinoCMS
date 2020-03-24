from django.contrib import admin
from .models import TimeTable, Session


@admin.register(TimeTable)
class MyAdmin(admin.ModelAdmin):
    pass


@admin.register(Session)
class MyAdmin(admin.ModelAdmin):
    pass
