from django.urls import path

from .views import UserViewSet

urlpatterns = [
#     path('users', UserViewSet.as_view({
#       'get': 'list',
#       'post': 'aaaa'
#     }))
    path('user', UserViewSet.as_view())
]
