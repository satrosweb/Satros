from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, Response
from .models import Employe, MainJob
from .serializers import EmployeSerializer, MainJobSerializer






class EmployeList(APIView):
    def get(seelf, request):
        instance = Employe.objects.all()
        ser = EmployeSerializer(instance=instance, many=True)
        return Response(data=ser.data)
        



class EmployeDetail(APIView):
    def get(self, request, job, name):
        instance = get_object_or_404(Employe, job=job, full_name=name)
        ser = EmployeSerializer(instance=instance)
        return Response(data=ser.data)
    