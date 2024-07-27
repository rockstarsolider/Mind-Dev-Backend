from rest_framework.views import APIView  
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from tasks import models, serializers
from django.conf import settings  

class CourseFazes(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request, format = None):
        course = models.Course.objects.first()
        fazes = models.Faze.objects.filter(course_id = course)
        faze_list = []
        for faze in fazes:
            faze_list.append(serializers.FazeSerializer(faze).data)
        response = [serializers.CourseSerializer(course).data,faze_list]
        return Response(response)

class FazeSections(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request, format = None, pk=None):
        faze = models.Faze.objects.get(pk=pk)
        sections = models.Section.objects.filter(faze_id=faze).order_by('section_number')
        sec_list= []
        for section in sections:
            sec_list.append(serializers.SectionSerializer(section).data)
        response = [serializers.FazeSerializer(faze).data,sec_list]
        return Response(response)