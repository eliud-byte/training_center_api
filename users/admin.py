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

    # --- SECURITY LOGIC BELOW ----
    def get_readonly_fields(self, request, obj=None):
        """
        Prevents non-superusers from promoting themselves or changing
        sensitive permissions.
        """
        if not request.user.is_superuser:
            # These fields will be visible but 'locked" (grayed out)
            return ('is_superuser', 'is_staff', 'user_permissions', 'groups')
        
        # Superusers can still edit everything as normal
        return super().get_readonly_fields(request, obj)

admin.site.register(User, CustomUserAdmin)
