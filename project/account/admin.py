from django.contrib import admin
from .models import CustomUser, Teacher, Student
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

admin.site.site_header = "Mind Dev"

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age','province','intro_method',)}),
    )

admin.site.register(CustomUser, MyUserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)