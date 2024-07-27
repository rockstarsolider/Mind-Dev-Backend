from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Faze(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_img_url = models.URLField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Section(models.Model):
    faze_id = models.ForeignKey(Faze, on_delete=models.CASCADE)
    section_number = models.PositiveSmallIntegerField()
    html_code = models.TextField(null=True, blank=True)
    js_code = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.faze_id.name+' Section: '+str(self.section_number)

class TaskFiles(models.Model):
    file = models.FileField(upload_to='tasks/')
    def __str__(self):
        return self.file.name