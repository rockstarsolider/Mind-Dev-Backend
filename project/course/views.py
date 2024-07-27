from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from account import models, serializers
from datetime import datetime
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
        do_task = StudentDoTask.objects.filter(student_course_group_member_id=membership).last().course_group_weekly_tasks_id.weekly_tasks_id
        if do_task.days_to_complete:  
            days_remaining = (do_task.days_to_complete - datetime.today().date()).days
        else:  
            days_remaining = None
        task = [student.user.first_name,WeeklyTaskSerializer(do_task).data,days_remaining]
        return Response(task)