from django.urls import path

# from google_sign import settings
from . import views
from django.urls.resolvers import URLPattern
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.loginPage, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("flowchart/", views.flowchart, name="flowchart"),
    path("step_1/", views.step_1, name="step_1"),
    path("step_2/", views.step_2, name="step_2"),
    path("step_3/", views.step_3, name="step_3"),
    path("step_4/", views.step_4, name="step_4"),
    path("step_5/", views.step_5, name="step_5"),
    path("step_6/", views.step_6, name="step_6"),
    path("step_7/", views.step_7, name="step_7"),
    path("step_8/", views.step_8, name="step_8"),
    path("team_portal/", views.team_portal, name="team_portal"),
    path("view_team/", views.view_team, name="view_team"),
    path("student_portal/", views.student_portal, name="student_portal"),
    path("student_profile/<str:pk>", views.student_profile, name="student_profile"),
    path("teacher_profile/", views.teacher_profile, name="teacher_profile"),
    path("survey/", views.survey, name="survey"),
    path("logbook_complete/", views.logbook_complete, name="logbook_complete"),
    path("check_email_exists/", views.check_email_exists, name="check_email_exists"),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="website/password_reset.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="website/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="website/password_reset_done.html"
        ),
        name="password_reset_complete",
    ),
]
