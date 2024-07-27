from django.contrib import admin
from .models import Course, Faze, Section, TaskFiles

admin.site.register(Course)
admin.site.register(Faze)
admin.site.register(Section)
admin.site.register(TaskFiles)