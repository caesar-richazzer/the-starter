from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'is_freelancer', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_freelancer',)}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)