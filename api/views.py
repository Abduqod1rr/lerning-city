from django.shortcuts import render
from .models import Lesson , boughtLessons
from .serializers import lesson_sz ,boughtlessons_sz
from .permissions import IsOwner , IsStudent
from rest_framework import generics

#
class createLesson(generics.CreateAPIView):

    queryset=Lesson.objects.all()
    serializer_class=lesson_sz

#
class lesson_crud(generics.RetrieveUpdateDestroyAPIView):
    
    queryset=Lesson.objects.all()
    serializer_class=lesson_sz
    permission_classes=[IsOwner]

#
class Buylessons(generics.CreateAPIView):
    queryset = boughtLessons.objects.all()
    serializer_class = boughtlessons_sz

class seeLessons(generics.RetrieveAPIView):

    
    queryset = boughtLessons.objects.all()
    serializer_class = boughtlessons_sz
    permission_classes = [IsStudent]