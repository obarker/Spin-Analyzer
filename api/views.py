from django.shortcuts import render
from rest_framework import serializers
from .serializers import UserSerializer
from .models import Users
from rest_framework import generics


# Create your views here.

class UserView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    