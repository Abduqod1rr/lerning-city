from rest_framework import serializers
from .models import Lesson , boughtLessons

class lesson_sz(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields = ['title' , 'price', 'content']