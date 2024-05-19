from django.contrib import admin
from .models import Task

class MyTask(admin.ModelAdmin):

    list_filter = ["completed"]
    list_display = ("title", "user", 'completed', 'created_at')
    search_fields = ("title",)

admin.site.register(Task, MyTask)