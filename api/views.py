from django.shortcuts import render
from .models import Lesson , boughtLessons
from .serializers import lesson_sz ,boughtlessons_sz
from .permissions import IsOwner , IsStudent
from rest_framework import generics

#creating lesson
class createLesson(generics.CreateAPIView):

    queryset=Lesson.objects.all()
    serializer_class=lesson_sz

#CRUD lessons
class lesson_crud(generics.RetrieveUpdateDestroyAPIView):
    
    queryset=Lesson.objects.all()
    serializer_class=lesson_sz
    permission_classes=[IsOwner]

#buy lesson
class Buylessons(generics.CreateAPIView):
    queryset = boughtLessons.objects.all()
    serializer_class = boughtlessons_sz

#home
class seeLessons(generics.ListAPIView):

    queryset=Lesson.objects.all()
    serializer_class=lesson_sz

#my bought lessons
class seeBoughtLessons(generics.ListAPIView):
    queryset = boughtLessons.objects.all()
    serializer_class = boughtlessons_sz
    permission_classes = [IsStudent]