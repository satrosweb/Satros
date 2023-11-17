from rest_framework import serializers
from .models import Employe, MainJob




class MainJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainJob
        fields = "__all__"




class EmployeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employe
        fields = "__all__"




