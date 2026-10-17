from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_home),
    path("run-weather/", views.run_weather, name="run_weather"),
]