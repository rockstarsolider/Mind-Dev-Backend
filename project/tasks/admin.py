from django.contrib import admin
from .models import Task

class taskAdminArea(admin.AdminSite):
    site_header = 'Tasks Admin Area'
    login_template = 'login.html'

task_admin_site = taskAdminArea(name='task admin')

class MyTask(admin.ModelAdmin):
    list_filter = ["completed", "created_at"]
    list_display = ("title", "user", 'completed', 'created_at')
    search_fields = ("title",)
    actions = ('mark_as_completed',)

    def mark_as_completed(self, request, queryset):
        queryset.update(completed=True)
        self.message_user(request, "Selected tasks have been marked as completed.")
    mark_as_completed.short_description = "Mark selected Tasks as completed"

    fieldsets=(
        ('Section 1:',{'fields':('user','completed',),'description':'description'}),
        ('Section 2:',{'fields':('title','description',),'classes':('collapse',)}),
    )

task_admin_site.register(Task, MyTask)