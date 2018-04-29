from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from project.api.serializers import UserSerializer, StudentSerializer, UniversitySerializer
from .models import University, Student
from rest_framework.views import APIView, Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    
class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Some Get Response")

    def post(self, request, format=None):
        return Response("Some Post Response")
