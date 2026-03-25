from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

# 1. Create an Inline for the Profile model
# This allows the Profile fields to appear on the User edit page
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile Info'

# 2. Define a new UserAdmin class that includes the Inline
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# 3. Re-register User: Unregister the default one first, then register yours
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# 4. (Optional) Register Profile separately if you want a dedicated list
# admin.site.register(Profile)