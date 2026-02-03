from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Options for role field
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        INSTRUCTOR = "INSTRUCTOR", "Instructor"
        STUDENT = "STUDENT", "Student"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    # We can add more profile fields here later if needed

    def save(self, *args, **kwargs):
        # If no role is set, default to the base_role
        if not self.pk and not self.role:
            self.role = self.base_role
        return super().save(*args, **kwargs)

