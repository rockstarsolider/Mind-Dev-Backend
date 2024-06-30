from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from djoser.views import UserViewSet
from .models import Teacher, Student, CustomUser
from .serializers import CustomUserSerializer, TeacherSerializer, StudentSerializer, CustomUserCreateSerializer, CvSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser

class UserViewSet(UserViewSet):
    serializer_class = CustomUserSerializer
    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserCreateView(APIView):
    def post(self, request, format=None):
        data = request.data.copy()
        serializer = CustomUserCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherViewSet(APIView):
    def get(self, request, *args, **kwargs):
        try:
            teacher = Teacher.objects.get(user=request.user)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def retrieve(self, request, *args, **kwargs):
        user_tasks = Student.objects.filter(user=request.user)
        serializer = self.get_serializer(user_tasks, many=True)
        return Response(serializer.data)
    
    def partial_update(self, request, pk=None, *args, **kwargs):
        try:
            student = self.get_object()
            if student.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = self.get_serializer(student, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UploadCV(APIView):
    serializer_class = CvSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, pk=None, queryset=None):
        request.user = Student.objects.filter(pk=pk).first()
        serializer = self.serializer_class(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)