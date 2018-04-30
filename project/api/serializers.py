from django.contrib.auth.models import User
from rest_framework import serializers
from .models import University, Student, Puppy

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = '__all__'
