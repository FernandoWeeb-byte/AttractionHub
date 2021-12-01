from django.urls import path

from .views import ManagerView

urlpatterns = [
    path('man/', ManagerView.as_view())
   
]