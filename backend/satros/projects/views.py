from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, Response
from .models import Project
from .serializers import ProjectSerializer


class ProjectList(APIView):
    def get(self, request):
        projects = Project.published.all()
        ser = ProjectSerializer(instance=projects, many=True)
        return Response(data=ser.data)



class ProjectDetail(APIView):
    def get(self, request, slug, pk):
        project = get_object_or_404(Project, 
                                    slug=slug, id=pk)
        ser = ProjectSerializer(instance=project)
        return Response(data=ser.data)
