from django.urls import path
from djoser import views as djoser_views
from .views import *

urlpatterns =[
    path('group/<int:pk>/', CourseGroupViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('<int:pk>/', CourseViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('term/<int:pk>/', TermViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('weekday/<int:pk>/', WeekDayViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('meeting/<int:pk>/', GroupMeetingViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('student_course_group/<int:pk>/', StudentCourseGroupViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('weekly_task/<int:pk>/', WeeklyTaskViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('image/<int:pk>/', ImageLinkViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('video/<int:pk>/', VideoLinkViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('group_task/<int:pk>/', CourseGroupWeeklyTaskViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('student_do_task/<int:pk>/', StudentDoTaskViewSet.as_view({'get': 'retrieve'}), name='user'),

    path('group_mates/', groupMate.as_view(), name='user'),
    path('meeting_day/', meetingApi.as_view(), name='user'),
    path('prev_tasks/', prevTasks.as_view(), name='user'),
    path('new_task/', newTask.as_view(), name='user'),
]