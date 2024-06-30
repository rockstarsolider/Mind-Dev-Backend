from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserType, Teacher, Student, CustomUser
from djoser.serializers import UserSerializer, UserCreateSerializer

User = get_user_model()  # Use the custom User model

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__' 

class CustomUserSerializer(UserSerializer):
    user_type = UserTypeSerializer(read_only=True) 
    phone_number = serializers.IntegerField(required=False) 

    class Meta(UserSerializer.Meta):
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            'id', 'user_type', 'phone_number','first_name','last_name','user_type_id'
        )

class TeacherSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True) 
    experties = serializers.CharField(max_length=256, required=False, allow_blank=True)

    class Meta:
        model = Teacher
        fields = ('user', 'experties')

class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True) 
    national_code = serializers.DecimalField(max_digits=10, decimal_places=0, required=False)
    mother_phone_number = serializers.DecimalField(max_digits=11, decimal_places=0, required=False)
    father_phone_number = serializers.DecimalField(max_digits=11, decimal_places=0, required=False)
    home_phone_number = serializers.DecimalField(max_digits=11, decimal_places=0, required=False)
    city = serializers.CharField(max_length=100, required=False, allow_blank=True)
    interets = serializers.CharField(max_length=256, required=False, allow_blank=True)
    degree = serializers.CharField(max_length=50, required=False, allow_blank=True)
    birth_date = serializers.DateField(required=False)


    class Meta:
        model = Student
        fields = ('user', 'national_code', 'mother_phone_number', 'father_phone_number',
                  'home_phone_number', 'city', 'interets', 'degree', 'birth_date')

class CustomUserCreateSerializer(UserCreateSerializer):
    user_type = serializers.CharField(required=False)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = tuple(UserCreateSerializer.Meta.fields) + ('user_type',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user_type_choice = validated_data.get('user_type', 'student')
        user_type, created = UserType.objects.get_or_create(type=user_type_choice)
        user.user_type_id = user_type
        user.save()

        if user_type_choice == 'student':
            Student.objects.create(user=user)
        elif user_type_choice == 'mentor':
            Teacher.objects.create(user=user)
        else:
            raise serializers.ValidationError('Invalid user type')

        return user

class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('cv',)