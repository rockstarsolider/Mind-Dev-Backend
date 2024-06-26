# Generated by Django 5.0.4 on 2024-06-09 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('course', '0003_coursegroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursegroup',
            name='second_mentor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_mentor', to='account.teacher'),
        ),
        migrations.CreateModel(
            name='CourseGroupWeeklyTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursegroup')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMeetings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hold_on_date', models.DateField(null=True)),
                ('guests_numbers', models.IntegerField(default=0)),
                ('course_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursegroup')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourseGroupMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursegroup')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDoTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_task', models.BooleanField(default=False)),
                ('attend_at_meeting', models.BooleanField(default=False)),
                ('course_group_weekly_tasks_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursegroupweeklytask')),
                ('student_course_group_member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.studentcoursegroupmembership')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('days_to_complete', models.IntegerField(default=0)),
                ('resources_links', models.CharField(blank=True, max_length=256, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='VideoLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=256)),
                ('weekly_task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.weeklytask')),
            ],
        ),
        migrations.CreateModel(
            name='ImageLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=256)),
                ('weekly_task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.weeklytask')),
            ],
        ),
        migrations.AddField(
            model_name='coursegroupweeklytask',
            name='weekly_tasks_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.weeklytask'),
        ),
    ]
