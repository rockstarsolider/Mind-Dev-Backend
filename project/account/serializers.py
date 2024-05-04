from rest_framework import serializers
from .models import CustomUser, Profile
from djoser.serializers import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['province','age']

class CustomUserSerializer(serializers.ModelSerializer):
    extra = ProfileSerializer(source='profile', required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'extra']

class CustomUserSerializerWithProfile(UserSerializer):
    profile = CustomUserSerializer()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('profile',)