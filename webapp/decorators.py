from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name="Students").exists():
                return redirect("logbook_portal")
            elif request.user.groups.filter(name="Teachers").exists():
                return redirect("teacher_profile")
            elif request.user.groups.filter(name="Admins").exists():
                return redirect("teacher_profile")
            elif request.user.groups.filter(name="Mentors").exists():
                return redirect("teacher_profile")
            elif request.user.groups.filter(name="Judges").exists():
                return redirect("teacher_profile")
            else:
                return HttpResponse('No Groups')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Not authorized")
        return wrapper_func
    return decorator