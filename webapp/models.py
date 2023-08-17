from django.db import models
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
# Create your models here.

student_group = Group.objects.get(name="Students")
teacher_group = Group.objects.get(name="Teachers")
judge_group = Group.objects.get(name="Judges")
mentor_group = Group.objects.get(name="Mentors")
admin_group = Group.objects.get(name="Admins")


class StudentProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username=models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    excited_about = models.CharField(max_length=200, default='')
    free_time = models.CharField(max_length=200, default='')
    fav_book = models.CharField(max_length=200, default='')
    fav_food = models.CharField(max_length=200, default='')
    profile_pic=models.ImageField(default='profilepics/images.png' ,null=True, blank=True)
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username=models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=20,null=True)
    inst_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True)
    profile_pic=models.ImageField(default='profilepics/images.png' ,null=True, blank=True)
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
