from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# This allows you to view/edit users in the browser
class CustomUserAdmin(UserAdmin):
    # 'fieldsets' controls the "Change User" page
    fieldsets = list(UserAdmin.fieldsets) + [
        ('Custom Fields', {'fields': ('role',)}),
    ]

    # 'add_fieldsets' controls the "Add User" page
    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        ('Custom Fields', {'fields': ('role',)}),
    ]
    # 'list_display' controls the columns in the user list
    list_display = list(UserAdmin.list_display) + ['role']

admin.site.register(User, CustomUserAdmin)
