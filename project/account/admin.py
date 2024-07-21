from django.contrib import admin
from .models import CustomUser, Teacher, Student, UserType
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

admin.site.site_header = "Mind Dev"
admin.site.index_title = "Mind Dev administration"
admin.site.site_title = "Mind Dev admin"

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type_id','phone_number',)}),
    )

admin.site.register(CustomUser, MyUserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(UserType)