from typing import TYPE_CHECKING, cast
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from django.db.models import QuerySet
from .models import Enrollment
from .serializers import EnrollmentSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

if TYPE_CHECKING:
    from users.models import User as UserType

class EnrollmentViewSet(viewsets.ModelViewSet):
    # Provide a base queryset so some DRF helpers and tools work
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated] # Only logged in users can access
    
    def get_queryset(self):  # type: ignore[override]
        # 1. If Admin/Instructor, show ALL enrollments
        user = cast("UserType", self.request.user)
        if user.is_staff or (hasattr(user, 'role') and user.role in ['ADMIN', 'INSTRUCTOR']):
            return Enrollment.objects.all()
        
        # 2. If Student, show ONLY their own enrollments
        return Enrollment.objects.filter(student=user)

    def perform_create(self, serializer):
        # Automatically set the 'student' field to the currently logged-in user
        # This prevents students from enrolling others.

        # Optional: specific check to ensure Instructors don't enroll themselves as students
        user = cast("UserType", self.request.user)
        if user.role == 'INSTRUCTOR':
            raise ValidationError("Instructors cannot enroll in courses")
        
        serializer.save(student=self.request.user)