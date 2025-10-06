from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializers
# Create your views here.

class userRegister(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializers

    
         

