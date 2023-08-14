from django.db import models
from django.contrib.auth.models import Group

# Create your models here.

student_group = Group.objects.get(name='Students')
teacher_group = Group.objects.get(name='Teachers')
judge_group = Group.objects.get(name='Judges')
mentor_group = Group.objects.get(name='Mentors')
admin_group = Group.objects.get(name='Admins')

class StudentProfile(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    GENDER=(('Male','Male'),('Female','Female'),('Others','Others'))
    gender=models.CharField(max_length=20, choices=GENDER)
    excited_about = models.CharField(max_length=200, null=True,blank=True)
    free_time = models.CharField(max_length=200, null=True,blank=True)
    fav_book = models.CharField(max_length=200, null=True,blank=True)
    fav_food = models.CharField(max_length=200, null=True,blank=True)
    def __str__(self):
        return self.first_name + " "+  self.last_name
