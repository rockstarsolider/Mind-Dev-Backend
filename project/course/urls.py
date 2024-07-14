from django.urls import path
from djoser import views as djoser_views
from .views import *

urlpatterns =[
    path('group_mates/', groupMate.as_view(), name='user'),
    path('meeting_day/', meetingApi.as_view(), name='user'),
    path('prev_tasks/', prevTasks.as_view(), name='user'),
    path('new_task/', newTask.as_view(), name='user'),
]