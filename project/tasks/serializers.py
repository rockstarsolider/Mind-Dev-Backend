from rest_framework import serializers
from .models import Course, Faze, Section

class CourseSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Course
        fields = '__all__'

class FazeSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Faze
        fields = '__all__' 

class SectionSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Section
        fields = '__all__' 