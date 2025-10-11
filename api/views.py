from django.shortcuts import render
from .models import Lesson , boughtLessons
from .serializers import lesson_sz ,boughtlessons_sz
from .permissions import IsOwner , IsStudent
from rest_framework import generics
from rest_framework.parsers import MultiPartParser , FormParser

#creating lesson
class createLesson(generics.CreateAPIView):

    queryset=Lesson.objects.all()
    serializer_class=lesson_sz
    parser_classes=[MultiPartParser, FormParser]

    def perform_create(self,serrializer):
        serrializer.save(owner=self.request.user)

#CRUD lessons
class lesson_crud(generics.RetrieveUpdateDestroyAPIView):
    
    queryset=Lesson.objects.all()
    serializer_class=lesson_sz
    permission_classes=[IsOwner]

#buy lesson
class Buylessons(generics.CreateAPIView):
    queryset = boughtLessons.objects.all()
    serializer_class = boughtlessons_sz

    def perform_create(self, serializer):
        lesson_id = self.kwargs.get('pk')  # <– mana shu joyda id ni olamiz
        lesson = Lesson.objects.get(pk=lesson_id)
        serializer.save(student=self.request.user, lesson=lesson)

#home
class seeLessons(generics.ListAPIView):

    queryset=Lesson.objects.all()
    serializer_class=lesson_sz

#my bought lessons
class seeBoughtLessons(generics.ListAPIView):
    queryset = boughtLessons.objects.all()
    serializer_class = boughtlessons_sz
    permission_classes = [IsStudent]