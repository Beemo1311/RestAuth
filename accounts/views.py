from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, AboutUsSerializer, AboutInfoSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import AboutUser


class AllUserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class AboutUserListApiView(generics.ListAPIView):
    queryset = AboutUser.objects.all()
    serializer_class = AboutInfoSerializer
    permission_classes = (IsAuthenticated,)


class AboutUserCreateApiView(generics.CreateAPIView):
    queryset = AboutUser.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = (IsAuthenticated,)