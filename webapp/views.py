from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import *

# Create your views here.

# ========================SIGNUP SIGNIN VIEWS========================
@unauthenticated
def register(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            email = request.POST.get("email")
            user_exists = User.objects.filter(username=username, email=email).exists()
            if user_exists:
                messages.error(
                    request,
                    "Username is already assosiated with another account",
                )
            else:
                password1 = request.POST.get("password1")
                password2 = request.POST.get("password2")
                if password1 != password2:
                    messages.error(request, "Passwords do not match")
                    return redirect("register")
                else:
                    my_user = User.objects.create_user(username, email, password1)
                    category = request.POST.get("category")
                    if category == "student":
                        my_user.groups.add(student_group)
                        StudentProfile.objects.create(
                            user=my_user,
                            email=my_user.email,
                            username=my_user.username,
                        )
                    elif category == "teacher":
                        my_user.groups.add(teacher_group)
                        TeacherProfile.objects.create(
                            user=my_user,
                            email=my_user.email,
                            username=my_user.username,
                        )
                    elif category == "judge":
                        my_user.groups.add(judge_group)
                    elif category == "admin":
                        my_user.groups.add(admin_group)
                    elif category == "mentor":
                        my_user.groups.add(mentor_group)
                    my_user.save()
                return redirect("login")
        except IntegrityError as e:
            messages.error(request, "Username already taken!")
    return render(request, "website/register.html")


@unauthenticated
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name="Students").exists():
                return redirect("student_portal")
            elif user.groups.filter(name="Teachers").exists():
                return redirect("teacher_profile")
            elif user.groups.filter(name="Admins").exists():
                return redirect("teacher_profile")
            elif user.groups.filter(name="Mentors").exists():
                return redirect("teacher_profile")
            elif user.groups.filter(name="Judges").exists():
                return redirect("teacher_profile")
            else:
                return HttpResponse("No Groups")
        else:
            messages.error(request, "Username or Password is incorrect!")
    return render(request, "website/login.html")


@unauthenticated
def check_email_exists(request):
    if request.method == "POST":
        email = request.POST.get("email")

        user_exists = User.objects.filter(email=email).exists()

        if user_exists:
            return redirect("reset_password")
        else:
            return HttpResponse("Email does not exist!")
    return render(request, "website/check_email_exists.html")


@login_required(login_url="/")
def logout_view(request):
    logout(request)
    return redirect("/")


# views.py
from .forms import *


# @login_required(login_url="/")
# @allowed_user(allowed_roles=["Students"])
# def create_logbook(request):
#     if request.method == "POST":
#         form = CreateLogbookForm(request.POST)
#         if form.is_valid():
#             logbook = form.save(commit=False)
#             logbook.creator = request.user  # Assuming you have authentication set up
#             logbook.save()
#             return redirect("course_outline", logbook.code)
#     else:
#         form = CreateLogbookForm()
#     context = {"form": form}
#     return render(request, "website/create_logbook.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def join_logbook(request):
    if request.method == "POST":
        form = JoinLogbookForm(request.POST)
        if form.is_valid():
            logbook_code = form.cleaned_data["logbook_code"]
            try:
                logbook = Logbook.objects.get(code=logbook_code)
                # Add logic to add the current user to the logbook participants
                return redirect("course_outline", logbook.id)
            except Logbook.DoesNotExist:
                form.add_error("logbook_code", "Logbook with this code does not exist.")
    else:
        form = JoinLogbookForm()
    context = {"form": form}
    return render(request, "website/join_logbook.html", context)


# ========================STUDENTS========================
@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def student_portal(request):
    student = request.user.studentprofile
    if request.method == "POST":
        form = CreateLogbookForm(request.POST)
        if form.is_valid():
            logbook = form.save(commit=False)
            logbook.creator = request.user  # Assuming you have authentication set up
            logbook.save()
            messages.success(request,'Logbook created')
            return redirect("course_outline", logbook.code)
    else:
        form = CreateLogbookForm()
    context = {"student": student,"form": form}
    return render(request, "website/student_portal.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def student_profile(request):
    student = request.user.studentprofile
    if request.method == "POST":
        first_name = request.POST.get("f_name")
        last_name = request.POST.get("l_name")
        gender = request.POST.get("gender")
        excited_about = request.POST.get("excited")
        free_time = request.POST.get("time")
        fav_book = request.POST.get("book")
        fav_food = request.POST.get("food")
        StudentProfile.objects.update(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            excited_about=excited_about,
            free_time=free_time,
            fav_book=fav_book,
            fav_food=fav_food,
        )
        return redirect("student_portal")
    context = {"student": student}
    return render(request, "website/student_profile.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def course_outline(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    return render(request, "website/outline.html",context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def record_of_invention(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    return render(request, "website/record_of_invention.html",context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def statement_of_originality(request,pk):
    logbook=Logbook.objects.get(code=pk)
    if request.method == "POST":
        return redirect("flowchart",logbook.code)
    context={'logbook':logbook}
    return render(request, "website/statement_of_originality.html",context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def flowchart(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    return render(request, "website/flowchart.html",context)


# ========================STEPS========================
@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_1(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    if request.method == "POST":
        return redirect("step_2",logbook.code)
    return render(request, "website/step_1.html",context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_2(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    if request.method == "POST":
        return redirect("step_3",logbook.code)
    return render(request, "website/step_2.html",context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_3(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    if request.method == "POST":
        return redirect("step_4",logbook.code)
    return render(request, "website/step_3.html",context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_4(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    if request.method == "POST":
        return redirect("step_5",logbook.code)
    return render(request, "website/step_4.html",context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_5(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    if request.method == "POST":
        return redirect("step_6",logbook.code)
    return render(request, "website/step_5.html",context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_6(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    if request.method == "POST":
        return redirect("step_7",logbook.code)
    return render(request, "website/step_6.html",context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_7(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    if request.method == "POST":
        return redirect("step_8",logbook.code)
    return render(request, "website/step_7.html",context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_8(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    if request.method == "POST":
        return redirect("survey",logbook.code)
    return render(request, "website/step_8.html",context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def survey(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    return render(request, "website/survey.html",context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def logbook_complete(request,pk):
    logbook=Logbook.objects.get(code=pk)
    context={'logbook':logbook}
    return render(request, "website/logbook_complete.html")


# ========================TEAMS========================
@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def team_portal(request):
    return render(request, "website/team_portal.html")


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def view_team(request):
    return render(request, "website/view_team.html")


# ========================TEACHERS========================
@login_required(login_url="/")
@allowed_user(allowed_roles=["Teachers"])
def teacher_profile(request):
    teacher = request.user.teacherprofile
    if request.method == "POST":
        first_name = request.POST.get("f_name")
        last_name = request.POST.get("l_name")
        gender = request.POST.get("gender")
        inst_name = request.POST.get("inst_name")
        phone = request.POST.get("phone")
        TeacherProfile.objects.update(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            inst_name=inst_name,
            phone=phone,
        )
        print(first_name, last_name, gender, inst_name, phone)
        return redirect("teacher_profile")
    context = {"teacher": teacher}
    return render(request, "website/teacher_profile.html", context)
