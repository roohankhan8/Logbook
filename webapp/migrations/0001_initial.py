# Generated by Django 4.2.4 on 2023-09-01 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('inst_name', models.CharField(blank=True, max_length=600, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profilepics/images.png', null=True, upload_to='')),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=600, null=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('excited_about', models.CharField(default='', max_length=600)),
                ('free_time', models.CharField(default='', max_length=600)),
                ('fav_book', models.CharField(default='', max_length=600)),
                ('fav_food', models.CharField(default='', max_length=600)),
                ('profile_pic', models.ImageField(blank=True, default='profilepics/images.png', null=True, upload_to='')),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(default='', max_length=8)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Logbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, unique=True)),
                ('title', models.CharField(max_length=20, null=True)),
                ('inventor', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('schoolnamegrade', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('member2', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('schoolnamegrade2', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('member3', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('schoolnamegrade3', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('member4', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('schoolnamegrade4', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('member5', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('schoolnamegrade5', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('member6', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('schoolnamegrade6', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('sig1', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('sig2', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('sig3', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('sig4', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('sig5', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('sig6', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('initial_problem', models.TextField(blank=True, default='', null=True)),
                ('selected_problem', models.TextField(blank=True, default='', null=True)),
                ('describe_problem', models.TextField(blank=True, default='', null=True)),
                ('specific_sol', models.TextField(blank=True, default='', null=True)),
                ('factors', models.TextField(blank=True, default='', null=True)),
                ('research', models.TextField(blank=True, default='', null=True)),
                ('blueprint', models.ImageField(blank=True, default='blueprints/images.png', null=True, upload_to='')),
                ('design_problem', models.TextField(blank=True, default='', null=True)),
                ('sol_design_problem', models.TextField(blank=True, default='')),
                ('green_sol', models.TextField(blank=True, default='', null=True)),
                ('materials', models.TextField(blank=True, default='', null=True)),
                ('findings', models.TextField(blank=True, default='', null=True)),
                ('credit', models.TextField(blank=True, default='', null=True)),
                ('prototype', models.TextField(blank=True, default='', null=True)),
                ('prototype_pic', models.ImageField(blank=True, default='prototypes/images.png', null=True, upload_to='')),
                ('notes', models.TextField(blank=True, default='', null=True)),
                ('testing', models.TextField(blank=True, default='', null=True)),
                ('invention', models.TextField(blank=True, default='', null=True)),
                ('positive', models.TextField(blank=True, default='', null=True)),
                ('negative', models.TextField(blank=True, default='', null=True)),
                ('nameinvention', models.TextField(blank=True, default='', null=True)),
                ('benefits', models.TextField(blank=True, default='', null=True)),
                ('price', models.TextField(blank=True, default='', null=True)),
                ('buy', models.TextField(blank=True, default='', null=True)),
                ('customer_age', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('customer_gender', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('customer_education', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('customer_house', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('customer_marital', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('other_notes', models.TextField(blank=True, default='', null=True)),
                ('note_title', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('note_desc', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('things_enjoyed', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('thanking', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('difficulty', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('future', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, default=list, related_name='joined_logbooks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
