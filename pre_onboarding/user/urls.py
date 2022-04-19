from django.urls import path

from user.views import UserListAPI

urlpatterns = [
    path('', UserListAPI.as_view(), name='user_list'),
]