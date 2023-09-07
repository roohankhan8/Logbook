from django.db import models
from django.contrib.auth.models import Group, User
from django.utils.crypto import get_random_string
# Create your models here.

student_group = Group.objects.get(name="Students")
teacher_group = Group.objects.get(name="Teachers")
judge_group = Group.objects.get(name="Judges")
mentor_group = Group.objects.get(name="Mentors")
admin_group = Group.objects.get(name="Admins")


class StudentProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=600, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    excited_about = models.CharField(max_length=600, default="")
    free_time = models.CharField(max_length=600, default="")
    fav_book = models.CharField(max_length=600, default="")
    fav_food = models.CharField(max_length=600, default="")
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
    inst_name = models.CharField(max_length=600, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(
        default="profilepics/images.png", null=True, blank=True
    )
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Logbook(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=8, unique=True)
    members = models.ManyToManyField(User, related_name='joined_logbooks', blank=True, default=list)

    title = models.CharField(max_length=20, null=True)

    inventor = models.CharField(max_length=20, default="", null=True, blank=True)
    schoolnamegrade = models.CharField(max_length=20, default="", null=True, blank=True)
    member2 = models.CharField(max_length=600, default="", null=True, blank=True)
    schoolnamegrade2 = models.CharField(max_length=20, default="", null=True, blank=True)
    member3 = models.CharField(max_length=600, default="", null=True, blank=True)
    schoolnamegrade3 = models.CharField(max_length=20, default="", null=True, blank=True)
    member4 = models.CharField(max_length=600, default="", null=True, blank=True)
    schoolnamegrade4 = models.CharField(max_length=20, default="", null=True, blank=True)
    member5 = models.CharField(max_length=600, default="", null=True, blank=True)
    schoolnamegrade5 = models.CharField(max_length=20, default="", null=True, blank=True)
    member6 = models.CharField(max_length=600, default="", null=True, blank=True)
    schoolnamegrade6 = models.CharField(max_length=20, default="", null=True, blank=True)
    sig1 = models.CharField(max_length=600, default="", null=True, blank=True)
    sig2 = models.CharField(max_length=600, default="", null=True, blank=True)
    sig3 = models.CharField(max_length=600, default="", null=True, blank=True)
    sig4 = models.CharField(max_length=600, default="", null=True, blank=True)
    sig5 = models.CharField(max_length=600, default="", null=True, blank=True)
    sig6 = models.CharField(max_length=600, default="", null=True, blank=True)

    initial_problem = models.TextField(
        default="", null=True, blank=True
    )

    selected_problem = models.TextField(
        default="", null=True, blank=True
    )
    describe_problem = models.TextField(
        default="", null=True, blank=True
    )
    specific_sol = models.TextField(default="", null=True, blank=True)

    factors = models.TextField(default="", null=True, blank=True)
    research = models.TextField(default="", null=True, blank=True)
    blueprint = models.ImageField(
        default="blueprints/images.png", null=True, blank=True
    )
    design_problem = models.TextField(default="", null=True, blank=True)
    sol_design_problem = models.TextField(
        default="", blank=True
    )
    green_sol = models.TextField(default="", null=True, blank=True)

    materials = models.TextField(default="", null=True, blank=True)
    findings = models.TextField(default="", null=True, blank=True)
    credit = models.TextField(default="", null=True, blank=True)

    prototype = models.TextField(default="", null=True, blank=True)
    prototype_pic = models.ImageField(
        default="prototypes/images.png", null=True, blank=True
    )
    notes = models.TextField(default="", null=True, blank=True)

    testing = models.TextField(default="", null=True, blank=True)
    invention = models.TextField(default="", null=True, blank=True)
    positive = models.TextField(default="", null=True, blank=True)
    negative = models.TextField(default="", null=True, blank=True)

    nameinvention = models.TextField(default="", null=True, blank=True)
    benefits = models.TextField(default="", null=True, blank=True)
    price = models.TextField(default="", null=True, blank=True)
    buy = models.TextField(default="", null=True, blank=True)
    customer_age = models.CharField(max_length=10,default="", null=True, blank=True)
    customer_gender = models.CharField(
        max_length=10, default="", null=True, blank=True
    )
    customer_education = models.CharField(
        max_length=600, default="", null=True, blank=True
    )
    customer_house = models.CharField(max_length=600, default="", null=True, blank=True)
    customer_marital = models.CharField(
        max_length=600, default="", null=True, blank=True
    )
    other_notes = models.TextField(default="", null=True, blank=True)
    
    note_title=models.CharField(max_length=20, default="", null=True, blank=True)
    note_desc=models.CharField(max_length=600, default="", null=True, blank=True)
    
    things_enjoyed=models.CharField(max_length=600, default="", null=True, blank=True)
    thanking=models.CharField(max_length=600, default="", null=True, blank=True)
    difficulty=models.CharField(max_length=600, default="", null=True, blank=True)
    future=models.CharField(max_length=600, default="", null=True, blank=True)

    data_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string(length=8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.code

    def add_member(self, user):
        self.members.add(user)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    code=models.CharField(max_length=8,default='')

    def __str__(self):
        return f"{self.sender} - {self.content}"
