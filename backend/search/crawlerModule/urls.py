from django.urls import path

from .views import CrawlerView

urlpatterns = [
    path('crawler/', CrawlerView.as_view() )
   
]
