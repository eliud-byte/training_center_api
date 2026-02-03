from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# This allows you to view/edit users in the browser
admin.site.register(User, UserAdmin)
