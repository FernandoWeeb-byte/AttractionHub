from django.urls import path
from .views import MlView

urlpatterns = [
   
    path('test/', MlView.as_view())
    
]
