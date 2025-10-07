from django.shortcuts import render
from .models import Lesson , boughtLessons
from .serializers import lesson_sz
from .permissions import IsOwner
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