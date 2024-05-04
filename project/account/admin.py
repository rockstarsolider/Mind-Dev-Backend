from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


# Re-register UserAdmin
admin.site.unregister(CustomUser)
admin.site.register(CustomUser, UserAdmin)