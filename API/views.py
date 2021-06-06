# views import APIView, Response, Serailizers, rest_framework, model

from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer
from .models import Users
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.

class UserView(generics.ListAPIView):                                                                           
    queryset = Users.objects.all()
    serializer_class = UserSerializer