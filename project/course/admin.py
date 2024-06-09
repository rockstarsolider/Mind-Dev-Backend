from django.contrib import admin
from .models import Course, Quiz, SubmitQuiz,Terms, WeekDays, CourseGroup, GroupMeetings, StudentDoTask, CourseGroupWeeklyTask, VideoLinks, ImageLinks, WeeklyTask, StudentCourseGroupMembership
# Register your models here.

class MySubQuiz(admin.ModelAdmin):
    search_fields = ("student_id",)
    list_display = ("student_id",'quiz_id','points','is_correct')
    list_filter = ["is_correct"]

class MyCourseGroupWeeklyTasks(admin.ModelAdmin):
    search_fields = ("weekly_tasks_id","course_group_id",)
    list_display = ("weekly_tasks_id","course_group_id",)

class MyCourseGroup(admin.ModelAdmin):
    search_fields = ("main_mentor_id",)
    list_display = ("main_mentor_id","meta_meeting_day","technical_meeting_day",'course_id','start_date')

class MyCourse(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title",'term_number')

class MyGroupMeetings(admin.ModelAdmin):
    list_display = ("course_group_id",'hold_on_date', 'guests_numbers')

class MyImageLinks(admin.ModelAdmin):
    search_fields = ("url",'weekly_task_id')
    list_display = ("url",'weekly_task_id')

class MyVideoLinks(admin.ModelAdmin):
    search_fields = ("url",'weekly_task_id')
    list_display = ("url",'weekly_task_id')

class MyStudentGroupMember(admin.ModelAdmin):
    search_fields = ("student_id",'course_group_id',)
    list_display = ("student_id",'course_group_id')

class MyStudentDoTask(admin.ModelAdmin):
    search_fields = ("course_group_weekly_tasks_id",)
    list_display = ("course_group_weekly_tasks_id",'completed_task', 'attend_at_meeting')
    list_filter = ['completed_task', 'attend_at_meeting']

class MyTerms(admin.ModelAdmin):
    search_fields = ("term_str",'term_num')
    list_display = ("term_str",'term_num')

class MyWeeklyDays(admin.ModelAdmin):
    search_fields = ("day_str",'da_num')
    list_display = ("day_str",'day_num')

class MyWeeklyTask(admin.ModelAdmin):
    search_fields = ("title",'description', 'course_id')
    list_display = ("title",'days_to_complete', 'course_id')

admin.site.register(SubmitQuiz, MySubQuiz)
admin.site.register(Quiz)

admin.site.register(Course, MyCourse)
admin.site.register(Terms,MyTerms)
admin.site.register(WeekDays,MyWeeklyDays)
admin.site.register(CourseGroup,MyCourseGroup)
admin.site.register(GroupMeetings, MyGroupMeetings)
admin.site.register(StudentCourseGroupMembership, MyStudentGroupMember)
admin.site.register(StudentDoTask, MyStudentDoTask)
admin.site.register(CourseGroupWeeklyTask, MyCourseGroupWeeklyTasks)
admin.site.register(VideoLinks, MyVideoLinks)
admin.site.register(ImageLinks, MyImageLinks)
admin.site.register(WeeklyTask, MyWeeklyTask)