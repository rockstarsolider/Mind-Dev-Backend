from rest_framework import serializers
from .models import Terms, WeekDays, Course, CourseGroup, GroupMeetings, StudentCourseGroupMembership, WeeklyTask, ImageLinks, VideoLinks, CourseGroupWeeklyTask, StudentDoTask

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = '__all__' 

class WeekDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekDays
        fields = '__all__' 

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__' 

class CourseGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseGroup
        fields = '__all__' 

class GroupMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMeetings
        fields = '__all__' 

class StudentCourseGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourseGroupMembership
        fields = '__all__' 

class WeeklyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyTask
        fields = '__all__' 

class ImageLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLinks
        fields = '__all__' 

class VideoLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLinks
        fields = '__all__' 

class CourseGroupWeeklyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseGroupWeeklyTask
        fields = '__all__' 

class StudentDoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDoTask
        fields = '__all__' 