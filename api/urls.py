from django.urls import path
from .views import DeathPrediction

urlpatterns = [
    path('api/death/', DeathPrediction.as_view(), name = 'death_prediction'),
]