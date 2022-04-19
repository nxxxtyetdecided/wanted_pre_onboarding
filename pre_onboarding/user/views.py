from rest_framework import generics

from user.models import User
from user.serializer import UserListSerializer


# 유저 목록 및 생성
class UserListAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
