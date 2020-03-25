from django.urls import path
from .views import poster


urlpatterns = [
    path('', poster),
]
