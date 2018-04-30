from django.contrib import admin

# Register your models here.
from .models import University, Student, Puppy

admin.site.register(University)
admin.site.register(Student)
admin.site.register(Puppy)
