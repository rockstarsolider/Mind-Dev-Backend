from django.db import models
from account.models import Teacher, Student

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class CourseGroup(models.Model):
    title = models.CharField(max_length=100)
    start = models.DateTimeField(auto_now_add=True)
    weekly_meetings_dates = models.CharField(max_length=100)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CourseEnroll(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    group_id = models.ForeignKey(CourseGroup, on_delete=models.CASCADE)

class Project(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.course_id)

class Faze(models.Model):
    name = models.CharField(max_length=100)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProjectDefinition(models.Model):
    name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_video = models.FileField(upload_to='media',null=True)
    project_code = models.TextField()
    project_image = models.FileField(upload_to='media',null=True)
    faze_id = models.ForeignKey(Faze, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SubmitProject(models.Model):
    submit_files_zip_link = models.CharField(max_length=100)
    submit_comments = models.TextField()
    course_enroll_id = models.ForeignKey(CourseEnroll, on_delete=models.CASCADE)
    project_defenition_id = models.ForeignKey(ProjectDefinition, on_delete=models.CASCADE)

class Section(models.Model):
    faze_id = models.ForeignKey(Faze, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.faze_id)

class Quiz(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)

class SubmitQuiz(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    points = models.IntegerField(default=0)