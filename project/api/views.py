from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from project.api.serializers import UserSerializer, StudentSerializer, UniversitySerializer, PuppySerializer
from .models import University, Student, Puppy
from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_puppy(request, pk):
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single puppy
    if request.method == 'GET':
        return Response({})
    # delete a single puppy
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single puppy
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_puppies(request):
    # get all puppies
    if request.method == 'GET':
        return Response({})
    # insert a new record for a puppy
    elif request.method == 'POST':
        return Response({})
