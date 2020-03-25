from django.contrib import admin
from .models import New


@admin.register(New)
class MyAdmin(admin.ModelAdmin):
    pass
