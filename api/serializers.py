from rest_framework import serializers
from .models import Lesson , boughtLessons

class lesson_sz(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username', read_only=True)
      # ✅ yoki ImageField

    class Meta:
        model=Lesson
        fields = ['title' , 'price', 'owner' ,'content']

class boughtlessons_sz(serializers.ModelSerializer):
    lesson = lesson_sz(read_only=True)
    student = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = boughtLessons
        fields= '__all__'
        read_only_fields = ['student', 'lesson']