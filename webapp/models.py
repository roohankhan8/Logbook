from datetime import date
from django.db import models
from django.contrib.auth.models import Group, User
from django.utils import timezone
# Create your models here.

student_group = Group.objects.get(name="Students")
teacher_group = Group.objects.get(name="Teachers")
judge_group = Group.objects.get(name="Judges")
mentor_group = Group.objects.get(name="Mentors")
admin_group = Group.objects.get(name="Admins")


class StudentProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    excited_about = models.CharField(max_length=200, default="")
    free_time = models.CharField(max_length=200, default="")
    fav_book = models.CharField(max_length=200, default="")
    fav_food = models.CharField(max_length=200, default="")
    profile_pic = models.ImageField(
        default="profilepics/images.png", null=True, blank=True
    )
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, null=True)
    inst_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(
        default="profilepics/images.png", null=True, blank=True
    )
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


from django.utils.crypto import get_random_string


class Logbook(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=8, unique=True)

    title = models.CharField(max_length=20, null=True)

    inventor = models.CharField(max_length=20, default="")
    schoolnamegrade = models.CharField(max_length=20, default="")
    description = models.CharField(max_length=200, default="")
    sig1 = models.CharField(max_length=200, default="")
    sig2 = models.CharField(max_length=200, default="")
    sig3 = models.CharField(max_length=200, default="")
    sig4 = models.CharField(max_length=200, default="")

    initial_problem = models.CharField(
        max_length=200, default=""
    )

    selected_problem = models.CharField(
        max_length=200, default=""
    )
    describe_problem = models.CharField(
        max_length=200, default=""
    )
    specific_sol = models.CharField(max_length=200, default="")

    factors = models.CharField(max_length=200, default="")
    research = models.CharField(max_length=200, default="")

    blueprint = models.CharField(max_length=200, default="")
    design_problem = models.CharField(max_length=200, default="")
    sol_design_problem = models.CharField(
        max_length=200, default=""
    )
    green_sol = models.CharField(max_length=200, default="")

    materials = models.CharField(max_length=200, default="")
    findings = models.CharField(max_length=200, default="")
    credit = models.CharField(max_length=200, default="")

    prototype = models.CharField(max_length=200, default="")
    prototype_pic = models.CharField(max_length=200, default="")
    notes = models.CharField(max_length=200, default="")

    testing = models.CharField(max_length=200, default="")
    invention = models.CharField(max_length=200, default="")
    positive = models.CharField(max_length=200, default="")
    negative = models.CharField(max_length=200, default="")

    nameinvention = models.CharField(max_length=200, default="")
    benefits = models.CharField(max_length=200, default="")
    price = models.CharField(max_length=200, default="")
    buy = models.CharField(max_length=200, default="")
    customer_age = models.CharField(max_length=200, default="")
    customer_gender = models.CharField(
        max_length=200, default=""
    )
    customer_education = models.CharField(
        max_length=200, default=""
    )
    customer_house = models.CharField(max_length=200, default="")
    customer_marital = models.CharField(
        max_length=200, default=""
    )
    other_notes = models.CharField(max_length=200, default="")
    
    note_title=models.CharField(max_length=20, default="")
    note_desc=models.CharField(max_length=200, default="")
    
    things_enjoyed=models.CharField(max_length=200, default="")
    thanking=models.CharField(max_length=200, default="")
    difficulty=models.CharField(max_length=200, default="")
    future=models.CharField(max_length=200, default="")

    data_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string(length=8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.code
