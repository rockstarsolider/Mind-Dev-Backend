from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(write_only=True)

    class Meta:
        model = Task
        fields = ['id', 'user_email', 'title', 'description', 'completed', 'created_at']

    def create(self, validated_data):
        user_email = validated_data.pop('user_email')
        user = get_user_model().objects.get(email=user_email)
        validated_data['user'] = user
        task = Task.objects.create(**validated_data)
        return task