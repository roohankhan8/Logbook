from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib import messages
from django.db import IntegrityError


from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required


from .models import (
    student_group,
    teacher_group,
    judge_group,
    mentor_group,
    admin_group,
)


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect("student_portal")
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
                    category = request.POST.get("category")
                    my_user = User.objects.create_user(username, email, password1)
                    my_user.save()
                    if category == "student":
                        my_user.groups.add(student_group)
                    elif category == "teacher":
                        my_user.groups.add(teacher_group)
                    elif category == "judge":
                        my_user.groups.add(judge_group)
                    elif category == "admin":
                        my_user.groups.add(admin_group)
                    elif category == "mentor":
                        my_user.groups.add(mentor_group)
                return redirect("login")
        except IntegrityError as e:
            messages.error(request, "Username already taken!")
    return render(request, "website/register.html")


def loginPage(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name="Students").exists():
            return redirect("student_portal")
        elif request.user.groups.filter(name="Teachers").exists():
            return redirect("student_portal")
        elif request.user.groups.filter(name="Admins").exists():
            return redirect("teacher_profile")
        elif request.user.groups.filter(name="Mentors").exists():
            return redirect("teacher_profile")
        elif request.user.groups.filter(name="Judges").exists():
            return redirect("teacher_profile")
        else:
            return HttpResponse("No Groups")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name="Students").exists():
                print("Done")
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
def student_portal(request):
    return render(request, "website/student_portal.html")


@login_required(login_url="/")
def student_profile(request):
    # if request.method == "POST":
    #     f_name = request.POST.get("f_name")
    #     l_name = request.POST.get("l_name")
    #     excited = request.POST.get("excited")
    #     time = request.POST.get("time")
    #     book = request.POST.get("book")
    #     food = request.POST.get("food")
    #     student = Student(
    #         f_name=f_name,
    #         l_name=l_name,
    #         excited=excited,
    #         time=time,
    #         book=book,
    #         food=food,
    #     )
    #     student.save()
    #     messages.success(request, "Profile Saved!")
    #     return redirect("student_portal")
    return render(request, "website/student_profile.html")


@login_required(login_url="/")
def teacher_profile(request):
    return render(request, "website/teacher_profile.html")


@login_required(login_url="/")
def logout_view(request):
    logout(request)
    return redirect("/")


@login_required(login_url="/")
def step_1(request):
    return render(request, "website/step_1.html")


@login_required(login_url="/")
def step_2(request):
    return render(request, "website/step_2.html")


@login_required(login_url="/")
def step_3(request):
    return render(request, "website/step_3.html")


@login_required(login_url="/")
def step_4(request):
    return render(request, "website/step_4.html")


@login_required(login_url="/")
def step_5(request):
    return render(request, "website/step_5.html")


@login_required(login_url="/")
def step_6(request):
    return render(request, "website/step_6.html")


@login_required(login_url="/")
def step_7(request):
    return render(request, "website/step_7.html")


@login_required(login_url="/")
def step_8(request):
    return render(request, "website/step_8.html")


@login_required(login_url="/")
def survey(request):
    return render(request, "website/survey.html")


@login_required(login_url="/")
def logbook_complete(request):
    return render(request, "website/logbook_complete.html")


# ========================STEPS========================
@login_required(login_url="/")
def team_portal(request):
    return render(request, "website/team_portal.html")


@login_required(login_url="/")
def view_team(request):
    return render(request, "website/view_team.html")
