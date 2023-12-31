import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import *
from .forms import *

# Create your views here.

# ========================SIGNUP, SIGNIN VIEWS========================
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
                return redirect("logbook_portal")
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


# ========================STUDENTS========================

@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def chat_page(request, pk):
    logbook = Logbook.objects.get(code=pk)
    if not request.user.is_authenticated:
        return redirect("login")
    context = {"logbook": logbook}
    return render(request, "website/chat_page.html", context)

@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def logbook_portal(request):
    form = CreateLogbookForm(request.POST)
    if request.method == "POST":
        joining=request.POST.get('join_code')
        if form.is_valid():
            logbook = form.save(commit=False)
            logbook.creator = request.user
            logbook.save()
            messages.success(request, "Logbook created")
            return redirect("course_outline", logbook.code)
        if len(joining)==8:
            try:
                logbook = Logbook.objects.get(code=joining)
                if request.user != logbook.creator: 
                    logbook.add_member(request.user)
                    messages.success(request, "You are now a member!")
                elif request.user in logbook.members:
                    messages.error(request, "You are already a member!")
                elif request.user==logbook.creator:
                    messages.error(request, "You are already the creator!")
                return redirect("course_outline", logbook.code)
            except Logbook.DoesNotExist:
                messages.error("Logbook with this code does not exist.")
                return redirect('logbook_portal')
        else:
            messages.error(request, "Invalid logbook code")
    context={'form':form}
    return render(request, "website/logbook_portal.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def logbooks(request, pk):
    created_logbooks = request.user.logbook_set.all()
    joined_logbooks = request.user.joined_logbooks.all()
    total_joined_logbooks = joined_logbooks.count() > 0
    total_created_logbooks = created_logbooks.count() > 0
    context = {
        "created_logbooks": created_logbooks,
        "joined_logbooks": joined_logbooks,
        "total_created_logbooks": total_created_logbooks,
        "total_joined_logbooks": total_joined_logbooks,
    }
    return render(request, "website/logbooks.html", context)


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
        return redirect("logbook_portal")
    context = {"student": student}
    return render(request, "website/student_profile.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def course_outline(request, pk):
    logbook = Logbook.objects.get(code=pk)
    context = {"logbook": logbook}
    return render(request, "website/outline.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def record_of_invention(request, pk):
    logbook = Logbook.objects.get(code=pk)
    context = {"logbook": logbook}
    return render(request, "website/record_of_invention.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def statement_of_originality(request, pk):
    logbook = Logbook.objects.get(code=pk)
    if request.method == "POST":
        inventor = request.POST.get("inventor")
        schoolnamegrade = request.POST.get("schoolnamegrade")
        member2=request.POST.get('member2')
        schoolnamegrade2 = request.POST.get("schoolnamegrade2")
        member3=request.POST.get('member3')
        schoolnamegrade3 = request.POST.get("schoolnamegrade3")
        member4=request.POST.get('member4')
        schoolnamegrade4 = request.POST.get("schoolnamegrade4")
        member5=request.POST.get('member5')
        schoolnamegrade5 = request.POST.get("schoolnamegrade5")
        member6=request.POST.get('member6')
        schoolnamegrade6 = request.POST.get("schoolnamegrade6")
        sig1 = request.POST.get("sig1")
        sig2 = request.POST.get("sig2")
        sig3 = request.POST.get("sig3")
        sig4 = request.POST.get("sig4")
        sig5 = request.POST.get("sig5")
        sig6 = request.POST.get("sig6")
        Logbook.objects.update(
            inventor=inventor,
            schoolnamegrade=schoolnamegrade,
            member2=member2,
            schoolnamegrade2=schoolnamegrade2,
            member3=member3,
            schoolnamegrade3=schoolnamegrade3,
            member4=member4,
            schoolnamegrade4=schoolnamegrade4,
            member5=member5,
            schoolnamegrade5=schoolnamegrade5,
            member6=member6,
            schoolnamegrade6=schoolnamegrade6,
            sig1=sig1,
            sig2=sig2,
            sig3=sig3,
            sig4=sig4,
            sig5=sig5,
            sig6=sig6,
        )
        return redirect("flowchart", logbook.code)
    context = {"logbook": logbook}
    return render(request, "website/statement_of_originality.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def flowchart(request, pk):
    logbook = Logbook.objects.get(code=pk)
    context = {"logbook": logbook}
    return render(request, "website/flowchart.html", context)


# ========================STEPS========================
@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_1(request, pk):
    logbook = Logbook.objects.get(code=pk)
    if request.method == "POST":
        initial_problem = request.POST.get("initial_problem")
        Logbook.objects.update(
            initial_problem=initial_problem,
        )
        return redirect("step_2", logbook.code)
    context = {"logbook": logbook}
    return render(request, "website/step_1.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_2(request, pk):
    logbook = Logbook.objects.get(code=pk)
    if request.method == "POST":
        selected_problem = request.POST.get("selected_problem")
        describe_problem = request.POST.get("describe_problem")
        specific_sol = request.POST.get("specific_sol")
        Logbook.objects.update(
            selected_problem=selected_problem,
            describe_problem=describe_problem,
            specific_sol=specific_sol,
        )
        return redirect("step_3", logbook.code)
    context = {"logbook": logbook}
    return render(request, "website/step_2.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_3(request, pk):
    logbook = Logbook.objects.get(code=pk)
    if request.method == "POST":
        factors = request.POST.get("factors")
        research = request.POST.get("research")
        Logbook.objects.update(
            factors=factors,
            research=research,
        )
        return redirect("step_4", logbook.code)
    context = {"logbook": logbook}
    return render(request, "website/step_3.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_4(request, pk):
    logbook = Logbook.objects.get(code=pk)
    if request.method == "POST":
        blueprint = request.POST.get("blueprint")
        design_problem = request.POST.get("design_problem")
        sol_design_problem = request.POST.get("sol_design_problem")
        green_sol = request.POST.get("green_sol")
        Logbook.objects.update(
            blueprint=blueprint,
            design_problem=design_problem,
            sol_design_problem=sol_design_problem,
            green_sol=green_sol,
        )

        return redirect("step_5", logbook.code)
    context = {"logbook": logbook}
    return render(request, "website/step_4.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_5(request, pk):
    logbook = Logbook.objects.get(code=pk)
    if request.method == "POST":
        materials = request.POST.get("materials")
        findings = request.POST.get("findings")
        credit = request.POST.get("credit")
        Logbook.objects.update(
            materials=materials,
            findings=findings,
            credit=credit,
        )
        return redirect("step_6", logbook.code)
    context = {"logbook": logbook}
    return render(request, "website/step_5.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_6(request, pk):
    logbook = Logbook.objects.get(code=pk)
    if request.method == "POST":
        prototype = request.POST.get("prototype")
        prototype_pic = request.POST.get("prototype_pic")
        notes = request.POST.get("notes")
        Logbook.objects.update(
            prototype=prototype,
            prototype_pic=prototype_pic,
            notes=notes,
        )
        return redirect("step_7", logbook.code)
    context = {"logbook": logbook}
    return render(request, "website/step_6.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_7(request, pk):
    logbook = Logbook.objects.get(code=pk)
    if request.method == "POST":
        testing = request.POST.get("testing")
        invention = request.POST.get("invention")
        positive = request.POST.get("positive")
        negative = request.POST.get("negative")
        Logbook.objects.update(
            testing=testing, invention=invention, positive=positive, negative=negative
        )
        return redirect("step_8", logbook.code)
    context = {"logbook": logbook}
    return render(request, "website/step_7.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def step_8(request, pk):
    logbook = Logbook.objects.get(code=pk)
    if request.method == "POST":
        nameinvention = request.POST.get("nameinvention")
        benefits = request.POST.get("benefits")
        price = request.POST.get("price")
        buy = request.POST.get("buy")
        customer_age = request.POST.get("customer_age")
        customer_gender = request.POST.get("customer_gender")
        customer_education = request.POST.get("customer_education")
        customer_house = request.POST.get("customer_house")
        customer_marital = request.POST.get("customer_marital")
        other_notes = request.POST.get("other_notes")

        # print(customer_age)
        # customer_age = int(customer_age)
        Logbook.objects.update(
            nameinvention=nameinvention,
            benefits=benefits,
            price=price,
            buy=buy,
            customer_age=customer_age,
            customer_gender=customer_gender,
            customer_education=customer_education,
            customer_house=customer_house,
            customer_marital=customer_marital,
            other_notes=other_notes,
        )
        return redirect("survey", logbook.code)
    context = {"logbook": logbook}
    return render(request, "website/step_8.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def delete_logbook(request, pk):
    logbook = Logbook.objects.get(code=pk)
    logbook.delete()
    return redirect("logbooks", request.user.username)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def survey(request, pk):
    logbook = Logbook.objects.get(code=pk)
    if request.method == "POST":
        things_enjoyed = request.POST.get("things_enjoyed")
        thanking = request.POST.get("thanking")
        difficulty = request.POST.get("difficulty")
        future = request.POST.get("future")
        Logbook.objects.update(
            things_enjoyed=things_enjoyed,
            thanking=thanking,
            difficulty=difficulty,
            future=future,
        )
        return redirect("logbook_complete", logbook.code)
    context = {"logbook": logbook}
    return render(request, "website/survey.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def logbook_complete(request, pk):
    logbook = Logbook.objects.get(code=pk)
    context = {"logbook": logbook}
    return render(request, "website/logbook_complete.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def notes(request, pk):
    logbook = Logbook.objects.get(code=pk)
    if request.method == "POST":
        note_title = request.POST.get("note_title")
        note_desc = request.POST.get("note_desc")
        Logbook.objects.update(
            note_title=note_title,
            note_desc=note_desc,
        )
        return redirect("notes", logbook.code)
    context = {"logbook": logbook}
    return render(request, "website/notes.html", context)


@login_required(login_url="/")
@allowed_user(allowed_roles=["Students"])
def preview_logbook(request, pk):
    logbook = Logbook.objects.get(code=pk)
    context = {"logbook": logbook}
    return render(request, "website/preview_logbook.html", context)


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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only if you don't need CSRF protection
def send_message(request,pk):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message')
            username = data.get('username')
            code=pk
            
            # Process the message (e.g., save it to the database)
            Message.objects.create(
                code=code ,
                sender=username,
                content=message
            )
            # Return a response, indicating success or failure
            response_data = {'status': 'success', 'message': 'Message sent successfully'}
            return JsonResponse(response_data)
        except Exception as e:
            response_data = {'status': 'error', 'message': str(e)}
            return JsonResponse("HI",response_data, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

