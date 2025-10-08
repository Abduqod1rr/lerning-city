from rest_framework import serializers
from .models import Lesson , boughtLessons

class lesson_sz(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields = ['title' , 'price', 'content']

class boughtlessons_sz(serializers.ModelSerializer):
    lesson = lesson_sz(read_only=True)
    student = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = boughtLessons
        fields= '__all__'