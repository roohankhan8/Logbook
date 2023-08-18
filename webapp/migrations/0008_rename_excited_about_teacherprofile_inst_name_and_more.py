# Generated by Django 4.2.4 on 2023-08-15 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_studentprofile_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherprofile',
            old_name='excited_about',
            new_name='inst_name',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='fav_book',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='fav_food',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='free_time',
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]