from django.urls import path
# from google_sign import settings
from . import views
from django.urls.resolvers import URLPattern
from django.contrib.auth import views as auth_views

urlpatterns = [
    #SIGNUP SIGNIN URLS
    path("", views.loginPage, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),

    #STUDENT'S URLS
    path("logbook_portal/", views.logbook_portal, name="logbook_portal"),
    path("student_profile/", views.student_profile, name="student_profile"),

    #LOGBOOK URLS
    # path("create_logbook/", views.create_logbook, name="create_logbook"),
    path("logbooks/<str:pk>/", views.logbooks, name="logbooks"),
    path("join_logbook/", views.join_logbook, name="join_logbook"),
    path("course_outline/<str:pk>/", views.course_outline, name="course_outline"),
    path("record_of_invention/<str:pk>/", views.record_of_invention, name="record_of_invention"),
    path("statement_of_originality/<str:pk>/", views.statement_of_originality, name="statement_of_originality"),
    path("flowchart/<str:pk>/", views.flowchart, name="flowchart"),
    path("step_1/<str:pk>/", views.step_1, name="step_1"),
    path("step_2/<str:pk>/", views.step_2, name="step_2"),
    path("step_3/<str:pk>/", views.step_3, name="step_3"),
    path("step_4/<str:pk>/", views.step_4, name="step_4"),
    path("step_5/<str:pk>/", views.step_5, name="step_5"),
    path("step_6/<str:pk>/", views.step_6, name="step_6"),
    path("step_7/<str:pk>/", views.step_7, name="step_7"),
    path("step_8/<str:pk>/", views.step_8, name="step_8"),
    path("survey/<str:pk>/", views.survey, name="survey"),
    path("notes/<str:pk>/", views.notes, name="notes"),
    path("logbook_complete/<str:pk>/", views.logbook_complete, name="logbook_complete"),
    path("delete_logbook/<str:pk>/", views.delete_logbook, name="delete_logbook"),
    path("preview_logbook/<str:pk>/", views.preview_logbook, name="preview_logbook"),

    #TEAMS URLS
    path("team_portal/", views.team_portal, name="team_portal"),
    path("view_team/", views.view_team, name="view_team"),

    #TEACHER'S URLS
    path("teacher_profile/", views.teacher_profile, name="teacher_profile"),

    #FORGOT PASSWORD URLS
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
