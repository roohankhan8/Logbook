from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from .models import *


# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.groups.filter(name="Students").exists():
#             StudentProfile.objects.create(
#                 user=instance, email=instance.email, username=instance.username
#             )
#             print('Student Created')
#         elif instance.groups.filter(name="Teachers").exists():
#             return
#         elif instance.groups.filter(name="Judges").exists():
#             return
#         elif instance.groups.filter(name="Admins").exists():
#             return
#         elif instance.groups.filter(name="Mentors").exists():
#             return
#         print("Profile created")
# post_save.connect(create_profile, sender=User)


# def update_profile(sender, instance, created, **kwargs):
#     if created == False:
#         if instance.groups.filter(name="Students").exists():
#             StudentProfile.objects.update(user=instance)
#             print('Student Updated')
#         elif instance.groups.filter(name="Teachers").exists():
#             return
#         elif instance.groups.filter(name="Judges").exists():
#             return
#         elif instance.groups.filter(name="Admins").exists():
#             return
#         elif instance.groups.filter(name="Mentors").exists():
#             return
#         # instance.studentprofile.save()
#         print("Profile updated")
# post_save.connect(update_profile, sender=User)
