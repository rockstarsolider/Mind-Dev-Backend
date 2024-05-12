from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsSuperUser
from rest_framework.decorators import action
from rest_framework.response import Response

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated, IsSuperUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def user_tasks(self, request, *args, **kwargs):
        user_tasks = Task.objects.filter(user=request.user)
        serializer = self.get_serializer(user_tasks, many=True)
        return Response(serializer.data)