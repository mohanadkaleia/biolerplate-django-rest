from django.db import models

# Create your models here.
class University(models.Model):
    # Start defining Univ's fields
    name = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    University = models.ForeignKey(University, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

class Puppy(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    breed = models.CharField(max_length = 255)
    color = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now_add=True)
    updateed_at = models.DateField(auto_now=True)

    def get_breed(self):
        return self.name + ' belongs to ' + self.breed + 'breed.'

    def __repr__(self):
        return self.name + ' is added.'
