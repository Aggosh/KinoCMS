from django.urls import path
from .views import movie, movies


urlpatterns = [
    path('', movies),
    path('<slug>/', movie),
]
