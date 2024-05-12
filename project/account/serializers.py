from rest_framework import serializers
from .models import CustomUser
from djoser.serializers import UserSerializer
from djoser.serializers import UserCreateSerializer
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'id', 'first_name', 'last_name', 'age', 'province', 'intro_method']

class CustomUserSerializerWithProfile(UserSerializer):
    profile = CustomUserSerializer()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('profile',)

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'username', 'province', 'intro_method', 'password')