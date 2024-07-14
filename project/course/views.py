from rest_framework.response import Response
from .models import CourseGroup, Course, Terms, WeekDays, GroupMeetings, StudentCourseGroupMembership, WeeklyTask, ImageLinks, VideoLinks, CourseGroupWeeklyTask, StudentDoTask
from .serializers import CourseGroupSerializer, CourseSerializer, TermSerializer, WeekDaySerializer, GroupMeetingSerializer, StudentCourseGroupSerializer, WeeklyTaskSerializer, ImageLinkSerializer, VideoLinkSerializer, CourseGroupWeeklyTaskSerializer, StudentDoTaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.views import APIView
from account import models, serializers

class TermViewSet(viewsets.ModelViewSet):
    queryset = Terms.objects.all()
    serializer_class = TermSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None, *args, **kwargs):
        term = Terms.objects.get(pk=pk)
        serializer = self.get_serializer(term)
        return Response(serializer.data)

class WeekDayViewSet(viewsets.ModelViewSet):
    queryset = WeekDays.objects.all()
    serializer_class = WeekDaySerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None, *args, **kwargs):
        weekday = WeekDays.objects.get(pk=pk)
        serializer = self.get_serializer(weekday)
        return Response(serializer.data)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None, *args, **kwargs):
        course = Course.objects.get(pk=pk)
        serializer = self.get_serializer(course)
        return Response(serializer.data)

class CourseGroupViewSet(viewsets.ModelViewSet):
    queryset = CourseGroup.objects.all()
    serializer_class = CourseGroupSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None, *args, **kwargs):
        group = CourseGroup.objects.get(pk=pk)
        serializer = self.get_serializer(group)
        return Response(serializer.data)

class GroupMeetingViewSet(viewsets.ModelViewSet):
    queryset = GroupMeetings.objects.all()
    serializer_class = GroupMeetingSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None, *args, **kwargs):
        meet = GroupMeetings.objects.get(pk=pk)
        serializer = self.get_serializer(meet)
        return Response(serializer.data)

class StudentCourseGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentCourseGroupMembership.objects.all()
    serializer_class = StudentCourseGroupSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None, *args, **kwargs):
        membership = StudentCourseGroupMembership.objects.get(pk=pk)
        serializer = self.get_serializer(membership)
        return Response(serializer.data)

class WeeklyTaskViewSet(viewsets.ModelViewSet):
    queryset = WeeklyTask.objects.all()
    serializer_class = WeeklyTaskSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None, *args, **kwargs):
        task = WeeklyTask.objects.get(pk=pk)
        serializer = self.get_serializer(task)
        return Response(serializer.data)
    
class ImageLinkViewSet(viewsets.ModelViewSet):
    queryset = ImageLinks.objects.all()
    serializer_class = ImageLinkSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None, *args, **kwargs):
        image = ImageLinks.objects.get(pk=pk)
        serializer = self.get_serializer(image)
        return Response(serializer.data)

class VideoLinkViewSet(viewsets.ModelViewSet):
    queryset = VideoLinks.objects.all()
    serializer_class = VideoLinkSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None, *args, **kwargs):
        video = VideoLinks.objects.get(pk=pk)
        serializer = self.get_serializer(video)
        return Response(serializer.data)

class CourseGroupWeeklyTaskViewSet(viewsets.ModelViewSet):
    queryset = CourseGroupWeeklyTask.objects.all()
    serializer_class = CourseGroupWeeklyTaskSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None, *args, **kwargs):
        group_task = CourseGroupWeeklyTask.objects.get(pk=pk)
        serializer = self.get_serializer(group_task)
        return Response(serializer.data)
    
class StudentDoTaskViewSet(viewsets.ModelViewSet):
    queryset = StudentDoTask.objects.all()
    serializer_class = StudentDoTaskSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def retrieve(self, request, pk=None, *args, **kwargs):
        do_task = StudentDoTask.objects.get(pk=pk)
        serializer = self.get_serializer(do_task)
        return Response(serializer.data)

class groupMate(APIView):
    Permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        student = models.Student.objects.filter(user=request.user).first()
        membership = StudentCourseGroupMembership.objects.filter(student_id=student).first()
        mates = StudentCourseGroupMembership.objects.filter(course_group_id = membership.course_group_id).all()
        serializer_data = []
        serializer_data.append(student.user.first_name)
        for mate in mates:
            a = models.Student.objects.filter(user = mate.student_id).first()
            serializer = serializers.StudentSerializer(a)
            serializer_data.append(serializer.data)
        return Response(serializer_data)

class meetingApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request, format=None):
        student = models.Student.objects.filter(user=request.user).first()
        membership = StudentCourseGroupMembership.objects.filter(student_id=student).first()
        meetings = GroupMeetings.objects.filter(course_group_id = membership.course_group_id).all()
        meets = []
        for meet in meetings:
            serialized = GroupMeetingSerializer(meet)
            meets.append(serialized.data)
        serializer = {'name':student.user.first_name,'meta':membership.course_group_id.meta_meeting_day.day_str, 'tech':membership.course_group_id.technical_meeting_day.day_str, 'meetings':meets}
        return Response(serializer)
    
class prevTasks(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request, format = None):
        student = models.Student.objects.filter(user=request.user).first()
        membership = StudentCourseGroupMembership.objects.filter(student_id=student).first()
        do_tasks = StudentDoTask.objects.filter(student_course_group_member_id=membership).all()
        tasks = []
        tasks.append(student.user.first_name)
        for do_task in do_tasks:
            task = WeeklyTaskSerializer(do_task.course_group_weekly_tasks_id.weekly_tasks_id).data
            if do_task.completed_task == True:
                tasks.append(task)
        return Response(tasks)

class newTask(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request, format = None):
        student = models.Student.objects.filter(user=request.user).first()
        membership = StudentCourseGroupMembership.objects.filter(student_id=student).first()
        do_task = StudentDoTask.objects.filter(student_course_group_member_id=membership).last()
        task = [student.user.first_name,WeeklyTaskSerializer(do_task.course_group_weekly_tasks_id.weekly_tasks_id).data]
        return Response(task)