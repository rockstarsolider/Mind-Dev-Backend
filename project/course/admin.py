from django.contrib import admin
from .models import Course, CourseGroup, CourseEnroll, Project, Faze, ProjectDefinition, SubmitProject, Section, Quiz, SubmitQuiz
# Register your models here.
class MyCourse(admin.ModelAdmin):
    list_filter = ["date_created"]
    list_display = ("name", "date_edited", 'date_created')
    search_fields = ("name",)

class MyCourseGroup(admin.ModelAdmin):
    list_filter = ["start"]
    list_display = ("title",'course_id','teacher_id', "weekly_meetings_dates", 'start')
    search_fields = ("title",)

class MyCourseEnroll(admin.ModelAdmin):
    list_display = ("group_id",'student_id')

class MyProject(admin.ModelAdmin):
    list_display = ("course_id",)

class MyFaze(admin.ModelAdmin):
    list_display = ('name',"project_id",)
    search_fields = ("name",)

class MyProjectDefinition(admin.ModelAdmin):
    list_display = ("name",'faze_id',)
    search_fields = ("name",)

class MySubmitProject(admin.ModelAdmin):
    list_display = ("course_enroll_id",'project_defenition_id',)
    
class MySection(admin.ModelAdmin):
    list_display = ("faze_id",)

class MyQuiz(admin.ModelAdmin):
    list_display = ("section_id",)

class MySubQuiz(admin.ModelAdmin):
    search_fields = ("student_id",)
    list_display = ("student_id",'quiz_id','points','is_correct')
    list_filter = ["is_correct"]

admin.site.register(Course, MyCourse)
admin.site.register(CourseGroup, MyCourseGroup)
admin.site.register(CourseEnroll, MyCourseEnroll)
admin.site.register(Project, MyProject)
admin.site.register(ProjectDefinition, MyProjectDefinition)
admin.site.register(Faze, MyFaze)
admin.site.register(SubmitQuiz, MySubQuiz)
admin.site.register(SubmitProject, MySubmitProject)
admin.site.register(Quiz, MyQuiz)
admin.site.register(Section, MySection)