from django.urls import path
from .views import AttractionView

urlpatterns = [
    path('attraction/', AttractionView.as_view()),
    path('attraction/<int:pk>/', AttractionView.as_view()),
]