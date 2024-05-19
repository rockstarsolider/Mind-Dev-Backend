# Generated by Django 5.0.4 on 2024-05-19 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_student'),
        ('course', '0003_alter_course_date_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_edited',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Faze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDefinition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('project_description', models.TextField()),
                ('project_video', models.FileField(null=True, upload_to='')),
                ('project_code', models.TextField()),
                ('project_image', models.FileField(null=True, upload_to='')),
                ('faze_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.faze')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faze_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.faze')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('correct_option', models.CharField(max_length=100)),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.section')),
            ],
        ),
        migrations.CreateModel(
            name='SubmitProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_files_zip_link', models.CharField(max_length=100)),
                ('submit_comments', models.TextField()),
                ('course_enroll_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.courseenroll')),
                ('project_defenition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.projectdefinition')),
            ],
        ),
        migrations.CreateModel(
            name='SubmitQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.quiz')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.student')),
            ],
        ),
    ]
