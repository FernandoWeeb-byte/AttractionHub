from django.urls import path
from .views import AttractionView, DatabaseView

urlpatterns = [
    path('attraction/', AttractionView.as_view()),
    path('attraction/<int:pk>/', AttractionView.as_view()),
    path('database/', DatabaseView.as_view())
]