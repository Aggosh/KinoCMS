from django.urls import path
from .views import new, news


urlpatterns = [
    path('', news),
    path('<slug>/', new),
]
