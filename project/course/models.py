from django.db import models
from account.models import Teacher, Student
from django_jalali.db import models as jmodels
 
# Create your models here.

class Terms(models.Model):
    term_num = models.IntegerField(null=True, blank=True)
    term_str = models.CharField(max_length=256, null=True, blank=True)
    
    def __str__(self):
        return str(self.term_str)

class WeekDays(models.Model):
    day_num = models.IntegerField(null=True, blank=True)
    day_str = models.CharField(max_length=256, null=True, blank=True)
    
    def __str__(self):
        return str(self.day_str)

class Course(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    term_number = models.ForeignKey(Terms, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.title)
    
class CourseGroup(models.Model):
    start_date = models.DateField(null=True)
    finish_date = models.DateField(null=True)
    edited_date = models.DateField(null=True)
    technical_meeting_day = models.ForeignKey(WeekDays, models.CASCADE)
    meta_meeting_day = models.ForeignKey(WeekDays, models.CASCADE,related_name='meta_meeting')
    course_id = models.ForeignKey(Course, models.CASCADE)
    main_mentor_id = models.ForeignKey(Teacher, models.CASCADE)
    second_mentor_id = models.ForeignKey(Teacher, models.CASCADE,related_name='second_mentor',null=True)

    def __str__(self):
        return str(self.main_mentor_id)+' group'

class GroupMeetings(models.Model):
    hold_on_date = jmodels.jDateField(null=True)
    guests_numbers = models.IntegerField(default=0)
    course_group_id = models.ForeignKey(CourseGroup, models.CASCADE)
    def __str__(self):
        return str(self.course_group_id.main_mentor_id)+str(self.hold_on_date)

class StudentCourseGroupMembership(models.Model):
    student_id = models.ForeignKey(Student, models.CASCADE)
    course_group_id = models.ForeignKey(CourseGroup, models.CASCADE)
    def __str__(self):
        return str(self.student_id)+str(self.course_group_id)
    
class WeeklyTask(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    days_to_complete = models.DateField(null=True)
    resources_links = models.CharField(max_length=256, null=True, blank=True)
    course_id = models.ForeignKey(Course, models.CASCADE)
    def __str__(self):
        return str(self.title)

class ImageLinks(models.Model):
    url = models.CharField(max_length=256)
    weekly_task_id = models.ForeignKey(WeeklyTask, models.CASCADE)
    def __str__(self):
        return str(self.weekly_task_id)
    
class VideoLinks(models.Model):
    url = models.CharField(max_length=256)
    weekly_task_id = models.ForeignKey(WeeklyTask, models.CASCADE)
    def __str__(self):
        return str(self.weekly_task_id)

class CourseGroupWeeklyTask(models.Model):
    weekly_tasks_id = models.ForeignKey(WeeklyTask, models.CASCADE)
    course_group_id = models.ForeignKey(CourseGroup, models.CASCADE)
    def __str__(self):
        return str(self.course_group_id)+'  '+str(self.weekly_tasks_id.title)

class StudentDoTask(models.Model):
    student_course_group_member_id = models.ForeignKey(StudentCourseGroupMembership, models.CASCADE)
    course_group_weekly_tasks_id = models.ForeignKey(CourseGroupWeeklyTask, models.CASCADE)
    completed_task = models.BooleanField(default=False)
    attend_at_meeting = models.BooleanField(default=False)

class Quiz(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)

class SubmitQuiz(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    def __str__(self):
        return str(self.student_id)+str( self.quiz_id)