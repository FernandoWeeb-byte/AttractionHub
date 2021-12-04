from django.urls import path

from .views import AnimeView, SerieView, SearchView

urlpatterns = [
    path('anime/', AnimeView.as_view()),
    path('serie/', SerieView.as_view()),
    path('search/', SearchView.as_view()),
]