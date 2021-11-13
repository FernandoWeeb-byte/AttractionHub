from django.urls import path

from .views import UserViewSet

urlpatterns = [
    path('users', UserViewSet.as_view({
      'post': 'registration',
      'get': 'get_user'
    })),
    # path('users/<str:pk>', UserViewSet.as_view({
    #   'get': 'get_user'
    # }))
]
